from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100, null=False, blank=False, validators=[
        RegexValidator(r'[A-Za-z0-9@#$%^&+=]{8,}',
                       message='The password must contain at least one in  A-Z and a-z, 0-9 and special character.')])
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)

# Create your models here.
