from django.db import models
from django.utils import timezone

class Shift(models.Model):
    ACCEPTED = 'accepted'
    PENDING = 'pending'
    REJECTED = 'rejected'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    ]

    agency = models.ForeignKey(
        'agencies.Agency',
        on_delete=models.CASCADE,
        related_name='posted_shifts'
    )
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    available_slots = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    accepted_users = models.ManyToManyField(
        to='users.User',
        related_name='accepted_shifts',
        blank=True
    )
    created_at = models.DateTimeField( default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    shift_location = models.CharField(max_length=200)
