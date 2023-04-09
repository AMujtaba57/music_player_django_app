from django.db import models
from django.contrib.auth.models import AbstractUser

class RegistrationUser(models.Model):
    email = models.CharField(max_length=250, unique=True, primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    password = models.CharField(max_length=250)
    is_superuser = models.BooleanField(default=False, null=True)
    username = models.CharField(max_length=250, blank=True)
    is_staff = models.BooleanField(default=False, null=True)
    is_active = models.BooleanField(default=False, null=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email