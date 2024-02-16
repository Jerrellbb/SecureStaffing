from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
  role = models.ForeignKey(
    to='roles.Role',
    on_delete=models.CASCADE,
    related_name='role',
    null=True
  )
  
