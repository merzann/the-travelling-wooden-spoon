# Generated by Django 4.2.17 on 2025-02-26 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_alter_recipe_excerpt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepagefeature',
            name='excerpt',
        ),
    ]
