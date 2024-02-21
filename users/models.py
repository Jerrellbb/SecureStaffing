from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
  role = models.ForeignKey(
    to='roles.Role',
    on_delete=models.CASCADE,
    related_name='role',
    
  )
  agency = models.ForeignKey(
        to='agencies.Agency',
        on_delete=models.CASCADE,
        related_name='owned_agency',
        null=True,
        blank=True
    )
  shifts = models.ForeignKey('shifts.Shift',on_delete=models.CASCADE, related_name='users',null=True, blank=True)
