# Generated by Django 5.0.2 on 2024-02-20 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('securityPersonnel', '0004_security_shift'),
    ]

    operations = [
        migrations.RenameField(
            model_name='security',
            old_name='shift',
            new_name='shifts',
        ),
    ]
