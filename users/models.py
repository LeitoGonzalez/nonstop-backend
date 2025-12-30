from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Usuario(AbstractUser):
    # podés agregar campos extras si querés
    pass

class Result(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wpm = models.PositiveIntegerField()
    accuracy = models.PositiveIntegerField()
    errors = models.PositiveIntegerField()
    score = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.wpm} WPM"