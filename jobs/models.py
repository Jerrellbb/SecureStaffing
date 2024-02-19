from django.db import models

# Create your models here.
class JobBid(models.Model):
  ACCEPTED = 'accepted'
  PENDING = 'pending'
  REJECTED = 'rejected'

  STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (ACCEPTED, 'Accepted'),
        (REJECTED, 'Rejected'),
    ]
  
  shift = models.ForeignKey('shifts.Shift', on_delete=models.CASCADE, related_name='job_bids')
  status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
  security_personnel = models.ForeignKey(
    to='securityPersonnel.security',
    on_delete=models.CASCADE,
    related_name='accepted_shifts',
  )

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)