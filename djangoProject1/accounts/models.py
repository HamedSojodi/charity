from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Gender_Choices = (
        ("m", "male"),
        ("f", "female"),
    )
    gender = models.CharField(max_length=1, choices=Gender_Choices, null=True, blank=True)
    phone = models.CharField(max_length=15)
    address = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(default=True)
    description = models.TextField(null=True, blank=True)
    last_login = models.DateTimeField(auto_now=True)


