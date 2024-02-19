# Generated by Django 5.0.2 on 2024-02-19 14:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agencies', '0002_rename_angency_agency'),
        ('shifts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shift',
            name='agency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posted_shifts', to='agencies.agency'),
        ),
    ]
