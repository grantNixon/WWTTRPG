# Generated by Django 5.0.1 on 2024-10-25 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0023_startingequipment_character_starting_equipment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='startingequipment',
            name='name',
            field=models.CharField(default='test', max_length=30),
            preserve_default=False,
        ),
    ]
