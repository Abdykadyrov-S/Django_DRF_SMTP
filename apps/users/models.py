from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email_confirmed = models.BooleanField(default=False)