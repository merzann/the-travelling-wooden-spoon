# Generated by Django 4.2.17 on 2024-12-18 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_recipe_thumbs_down_remove_recipe_thumbs_up_and_more'), ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='rating_count',
            field=models.IntegerField(
                default=0),
        ),
        migrations.AddField(
            model_name='recipe',
            name='total_rating',
            field=models.DecimalField(
                decimal_places=2,
                default=0.0,
                max_digits=5),
        ),
    ]
