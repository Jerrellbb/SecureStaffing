# Generated by Django 5.0.2 on 2024-02-26 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('securityPersonnel', '0006_remove_security_shifts'),
    ]

    operations = [
        migrations.AddField(
            model_name='security',
            name='image',
            field=models.URLField(blank=True, null=True),
        ),
    ]