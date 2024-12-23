# Generated by Django 4.2.17 on 2024-12-19 18:56

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id',
                 models.BigAutoField(
                     auto_created=True,
                     primary_key=True,
                     serialize=False,
                     verbose_name='ID')),
                ('bio',
                 models.TextField()),
                ('profile_picture',
                 cloudinary.models.CloudinaryField(
                     blank=True,
                     max_length=255,
                     null=True,
                     verbose_name='image')),
            ],
        ),
    ]
