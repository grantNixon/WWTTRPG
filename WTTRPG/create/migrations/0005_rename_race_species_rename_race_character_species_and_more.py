# Generated by Django 5.0.1 on 2024-05-21 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0004_alter_character_agility_alter_character_gumption_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Race',
            new_name='Species',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='race',
            new_name='species',
        ),
        migrations.RenameField(
            model_name='species',
            old_name='RaceName',
            new_name='SpeciesName',
        ),
    ]
