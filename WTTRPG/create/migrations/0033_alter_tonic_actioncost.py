# Generated by Django 5.0.1 on 2024-11-15 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0032_tonic_delete_tonics'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tonic',
            name='ActionCost',
            field=models.TextField(),
        ),
    ]