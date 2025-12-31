# Nonstop Typing Backend

Backend del proyecto Nonstop Typing App, encargado de la autenticación de usuarios, persistencia de resultados y exposición de endpoints para el frontend.
Construido con Django y Django REST Framework, incluye soporte para JWT y OAuth con Google.

## Funcionalidades

- Registro y login de usuarios (con soporte para Google OAuth)
- Autenticación mediante JWT
- Persistencia de resultados de mecanografía por usuario
- Historial de sesiones y métricas (WPM, precisión, errores, puntaje)
- API REST para comunicación con el frontend
- Configuración de CORS para permitir integración con el cliente React

## Tecnologías utilizadas

- Django (framework principal)
- Django REST Framework (API REST)
- djangorestframework-simplejwt (autenticación JWT)
- django-allauth (login social con Google)
- django-cors-headers (manejo de CORS)
- SQLite (base de datos local por defecto)
- Requests / Cryptography (dependencias para OAuth y seguridad)

## Instalación del Backend

```bash
git clone https://github.com/tu-usuario/nonstop-Backend.git
cd nonstop-Backend
python -m venv .venv
.venv\Scripts\activate # En Windows PowerShell
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

El backend se ejecuta por defecto en: http://127.0.0.1:8000

## Endpoints principales
- POST /api/google-login/ → Login con Google OAuth.
- POST /api/token/ → Login con credenciales tradicionales (JWT, vía SimpleJWT).
- POST /register/ → Registro de usuario
- GET /results/history → Historial de resultados del usuario autenticado (requiere JWT).
- POST /results/ → Guardar nueva sesión de mecanografía (requiere JWT).

## Uso con el frontend
El frontend (nonstop-Frontend) puede funcionar en modo local sin backend (guardando datos en localStorage).
Con el backend activo, se habilitan:
- Registro y login de usuarios.
- Persistencia de resultados en base de datos.
- Historial sincronizado entre dispositivos.

## Estado Del proyecto
Proyecto en desarrollo.
El backend ya soporta autenticación y persistencia de resultados, y se continúa trabajando en endpoints adicionales y mejoras de seguridad.

### Autor
Desarrollado por Leo.
