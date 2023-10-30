from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class UserData(AbstractUser):
    phone_number = models.CharField(max_length=13)
    address = models.CharField(max_length=255)
