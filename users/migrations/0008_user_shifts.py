# Generated by Django 5.0.2 on 2024-02-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0003_shift_available_slots'),
        ('users', '0007_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='shifts',
            field=models.ManyToManyField(related_name='accepted_shifts', to='shifts.shift'),
        ),
    ]
