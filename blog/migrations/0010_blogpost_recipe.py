# Generated by Django 4.2.17 on 2024-12-20 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_blogpost_title_alter_recipe_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='recipe',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name='blog_posts',
                to='blog.recipe'),
        ),
    ]
