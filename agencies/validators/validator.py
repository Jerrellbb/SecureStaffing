from django.core.validators import RegexValidator
from django.db import models

phone_number_validator = RegexValidator(
    regex=r'^(\+\d{1,3})?[\s.-]?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$',
    message='Please enter a valid phone number.',
)
