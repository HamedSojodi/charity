from django.db import models

from accounts.models import User


class Benefactor(models.Model):
    CHOICES = (
        ('0', 'low'),
        ('1', 'midlevel'),
        ('2', 'advanced'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    experience = models.SmallIntegerField(choices=CHOICES, default='0')
    free_time_per_week = models.PositiveSmallIntegerField(default='0')


class Charity(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)


class Task(models.Model):
    CHOICES = (
        ('P', 'Pending'),
        ('W', 'Waiting'),
        ('A', 'Assigned'),
        ('D', 'Done'),
    )
    CHOICES2 = (
        ('M','Male'),
        ('F','Female'),

    )
    assigned_benefactor = models.ForeignKey(Benefactor, on_delete=models.SET_NULL, blank=True,
                                            null=True, )
    charity = models.ForeignKey(Charity, models.CASCADE)
    state = models.CharField(max_length=1, choices=CHOICES, default='P')
    gender_limit = models.CharField(max_length=1, choices=CHOICES2)
    titel = models.CharField(max_length=100)
