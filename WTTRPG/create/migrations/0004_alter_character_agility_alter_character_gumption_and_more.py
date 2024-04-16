# Generated by Django 5.0.1 on 2024-04-13 16:52

import create.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0003_skill_character_gumption_character_intelligence_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='agility',
            field=models.IntegerField(choices=create.models.get_pointbuys),
        ),
        migrations.AlterField(
            model_name='character',
            name='gumption',
            field=models.IntegerField(choices=create.models.get_pointbuys),
        ),
        migrations.AlterField(
            model_name='character',
            name='intelligence',
            field=models.IntegerField(choices=create.models.get_pointbuys),
        ),
        migrations.AlterField(
            model_name='character',
            name='mysticism',
            field=models.IntegerField(choices=create.models.get_pointbuys),
        ),
        migrations.AlterField(
            model_name='character',
            name='personality',
            field=models.IntegerField(choices=create.models.get_pointbuys),
        ),
        migrations.AlterField(
            model_name='character',
            name='strength',
            field=models.IntegerField(choices=create.models.get_pointbuys),
        ),
    ]
