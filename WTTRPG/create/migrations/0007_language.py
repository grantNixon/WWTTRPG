# Generated by Django 5.0.1 on 2024-05-21 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0006_morals'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languageName', models.CharField(max_length=30)),
                ('languageDescription', models.CharField(max_length=300)),
            ],
        ),
    ]
