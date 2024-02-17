# Generated by Django 5.0.2 on 2024-02-16 18:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0001_initial'),
        ('users', '0002_alter_user_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='role', to='roles.role'),
        ),
    ]