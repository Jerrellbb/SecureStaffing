# Generated by Django 5.0.2 on 2024-02-19 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shifts', '0002_alter_shift_agency'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='available_slots',
            field=models.IntegerField(default=1),
        ),
    ]
