# Generated by Django 5.0.2 on 2024-02-20 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_user_shifts'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='shifts',
        ),
    ]