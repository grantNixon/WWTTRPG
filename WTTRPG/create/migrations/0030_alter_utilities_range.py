# Generated by Django 5.0.1 on 2024-11-15 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0029_alter_spell_actioncost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilities',
            name='Range',
            field=models.CharField(max_length=100),
        ),
    ]
