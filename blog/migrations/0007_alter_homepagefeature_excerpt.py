# Generated by Django 4.2.17 on 2024-12-19 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagefeature',
            name='excerpt',
            field=models.TextField(max_length=300),
        ),
    ]