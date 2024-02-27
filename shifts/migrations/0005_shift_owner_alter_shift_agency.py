# Generated by Django 5.0.2 on 2024-02-27 18:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencies', '0002_rename_angency_agency'),
        ('shifts', '0004_shift_accepted_users_shift_created_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_shift', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shift',
            name='agency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posted_shifts', to='agencies.agency'),
        ),
    ]