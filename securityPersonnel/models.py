from django.db import models

# Create your models here.
class Security(models.Model):
  name = models.CharField(max_length=50)
  experience = models.IntegerField()
  user = models.ForeignKey(
    to='users.User',
    on_delete=models.CASCADE,
    related_name='user',
    null=True
  )
  qualifications = models.ForeignKey(
    to='qualifications.Qualification',
    on_delete=models.CASCADE,
    related_name='owned_qualifications',
    null=True
  )