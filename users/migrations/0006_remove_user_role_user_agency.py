# Generated by Django 5.0.2 on 2024-02-19 17:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencies', '0002_rename_angency_agency'),
        ('users', '0005_remove_user_agency_user_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.AddField(
            model_name='user',
            name='agency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_agency', to='agencies.agency'),
        ),
    ]
