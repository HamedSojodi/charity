from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Gender_Choices = (
        ("m","male"),
        ("f","female"),
    )
    gender = models.CharField(max_length=1, choices=Gender_Choices)
    phone = models.CharField(max_length=15)
