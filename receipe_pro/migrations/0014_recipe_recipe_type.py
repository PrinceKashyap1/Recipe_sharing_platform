# Generated by Django 5.0.6 on 2024-07-08 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receipe_pro', '0013_alter_recipe_recipe_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_type',
            field=models.CharField(default='', max_length=100),
        ),
    ]
