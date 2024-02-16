from django.db import models
from .validators.validator import phone_number_validator
# Create your models here.
class Angency(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField(null=True, blank=True)
  phone_number = models.CharField(max_length=30,validators=[phone_number_validator])
  image = models.URLField(null=True, blank=True)
  owner = models.ForeignKey(
    to='users.User',
    on_delete=models.CASCADE,
    related_name='owned_agency',
    null=True
  )