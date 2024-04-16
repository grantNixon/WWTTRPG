# Generated by Django 5.0.1 on 2024-04-13 15:40

import create.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0002_armor_background_race_spell_tonics_utilities_weapon_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skillName', models.CharField(max_length=30)),
                ('skillAttribute', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='gumption',
            field=models.IntegerField(choices='', default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='intelligence',
            field=models.IntegerField(choices='', default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='majorskill1',
            field=models.CharField(choices=create.models.get_skills, default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='majorskill2',
            field=models.CharField(choices=create.models.get_skills, default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='majorskill3',
            field=models.CharField(choices=create.models.get_skills, default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='minorskill1',
            field=models.CharField(choices=create.models.get_skills, default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='minorskill2',
            field=models.CharField(choices=create.models.get_skills, default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='minorskill3',
            field=models.CharField(choices=create.models.get_skills, default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='minorskill4',
            field=models.CharField(choices=create.models.get_skills, default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='minorskill5',
            field=models.CharField(choices=create.models.get_skills, default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='mysticism',
            field=models.IntegerField(choices='', default=0),
        ),
        migrations.AddField(
            model_name='character',
            name='personality',
            field=models.IntegerField(choices='', default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='agility',
            field=models.IntegerField(choices='', default=0),
        ),
        migrations.AlterField(
            model_name='character',
            name='strength',
            field=models.IntegerField(choices='', default=0),
        ),
    ]