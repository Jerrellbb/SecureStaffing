from django.db import models

# Create your models here.
class Shift(models.Model):
    agency = models.ForeignKey(
        'agencies.Agency',
        on_delete=models.CASCADE,
        related_name='posted_shifts')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    available_slots = models.IntegerField(default=1)

