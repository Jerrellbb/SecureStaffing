# Generated by Django 5.0.2 on 2024-02-20 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityPersonnel', '0005_rename_shift_security_shifts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='security',
            name='shifts',
        ),
    ]
