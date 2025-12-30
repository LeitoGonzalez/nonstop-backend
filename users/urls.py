from django.urls import path
from . import views
from .views import google_login, register_user 
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('results/', views.save_result, name='save_result'),   # POST
    path('results/history/', views.list_results, name='list_results'),  # GET
    path("register/", register_user, name="register"),
    path("api/google-login/", google_login, name="google-login"), 
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
]