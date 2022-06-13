from django.db import models
from django.contrib.auth.models import AbstractUser

from accounts.validators import phone_validator


class User(AbstractUser):
    class Gender(models.TextChoices):
        MALE = 'M', 'Male'
        FEMALE = 'F', 'Female'
        UNSET = 'MF', 'Unset'
    gender = models.CharField(max_length=2, choices=Gender.choices, default=Gender.UNSET, null=True, blank=True)
    phone = models.CharField(max_length=15, validators=[phone_validator], blank=True)
    address = models.TextField(null=True, blank=True)
    age = models.PositiveSmallIntegerField(default=True, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    last_login = models.DateTimeField(auto_now=True)
    first_name = models.CharField(max_length=100)

    @property
    def is_benefactor(self):
        return hasattr(self, 'benefactor')

    @property
    def is_charity(self):
        return hasattr(self, 'charity')



