# Generated by Django 5.0.2 on 2024-02-16 20:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qualifications', '0001_initial'),
        ('securityPersonnel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='security',
            name='qualifications',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owned_qualifications', to='qualifications.qualification'),
        ),
    ]
