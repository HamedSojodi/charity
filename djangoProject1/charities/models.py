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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=50)
    reg_number = models.CharField(max_length=10)


class TaskManager(models.Manager):
    def related_tasks_to_charity(self, user):
        return self.filter(charity__user=user)

    def related_tasks_to_benefactor(self, user):
        return self.filter(assigned_benefactor__user=user)

    def all_related_tasks_to_user(self, user):
        charity_tasks = self.related_tasks_to_charity(user)
        benefactor_tasks = self.related_tasks_to_benefactor(user)
        benefactor_tasks = self.related_tasks_to_charity(user)


class Task(models.Model):
    CHOICES = (
        ('P', 'Pending'),
        ('W', 'Waiting'),
        ('A', 'Assigned'),
        ('D', 'Done'),
    )
    CHOICES2 = (
        ('M', 'Male'),
        ('F', 'Female'),

    )

    assigned_benefactor = models.ForeignKey(Benefactor, on_delete=models.SET_NULL, blank=True,
                                            null=True, related_name='benfactor')
    charity = models.ForeignKey(Charity, models.CASCADE, related_name='charti')
    state = models.CharField(max_length=1, choices=CHOICES, default='P')
    gender_limit = models.CharField(max_length=1, choices=CHOICES2, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(null=True, blank=True)
    age_limit_from = models.IntegerField(null=True, blank=True)
    age_limit_to = models.IntegerField(null=True, blank=True)
    titel = models.CharField(max_length=100)
    objects = TaskManager()
