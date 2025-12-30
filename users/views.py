from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import ResultSerializer
from .models import Result
import requests
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError

User = get_user_model()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def save_result(request):
    serializer = ResultSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def list_results(request):
    results = Result.objects.filter(user=request.user).order_by('-date')
    serializer = ResultSerializer(results, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def register_user(request):
    username = request.data.get("username", "").strip()
    email = request.data.get("email", "").strip()
    password = request.data.get("password", "")

    if not username or not password:
        return Response(
            {"error": "Username y password requeridos"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(username__iexact=username).exists():
        return Response(
            {"error": "El nombre de usuario ya está en uso"},
            status=status.HTTP_400_BAD_REQUEST
        )

    if email and User.objects.filter(email__iexact=email).exists():
        return Response(
            {"error": "Ya existe una cuenta con ese email"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        validate_password(password)
    except ValidationError as e:
        return Response(
            {"error": e.messages[0]},
            status=status.HTTP_400_BAD_REQUEST
        )

    user = User.objects.create_user(
        username=username,
        email=email,
        password=password
    )

    return Response(
        {"message": "Usuario creado correctamente"},
        status=status.HTTP_201_CREATED
    )

@api_view(["POST"])
def google_login(request):
    token = request.data.get("token")
    if not token:
        return Response({"error": "Token requerido"}, status=status.HTTP_400_BAD_REQUEST)

    # Validar token con Google
    resp = requests.get("https://oauth2.googleapis.com/tokeninfo", params={"id_token": token})
    if resp.status_code != 200:
        return Response({"error": "Token inválido"}, status=status.HTTP_400_BAD_REQUEST)

    data = resp.json()
    email = data.get("email")
    if not email:
        return Response({"error": "Email no encontrado"}, status=status.HTTP_400_BAD_REQUEST)

    # Crear o recuperar usuario usando tu modelo personalizado
    user, _ = User.objects.get_or_create(username=email, defaults={"email": email})

    # Generar JWT propio
    refresh = RefreshToken.for_user(user)
    return Response({
        "access": str(refresh.access_token),
        "refresh": str(refresh),
        "username": user.username,
    })
