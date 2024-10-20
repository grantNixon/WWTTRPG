# Generated by Django 5.0.1 on 2024-10-20 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0022_rename_sk_handtohand_character_sk_hand'),
    ]

    operations = [
        migrations.CreateModel(
            name='StartingEquipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemList', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='character',
            name='starting_equipment',
            field=models.CharField(default='fuck', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='starting_weapon',
            field=models.CharField(default='you', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_absolutionmagic',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_acrobatics',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_animalhandling',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_archery',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_athletics',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_barter',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_brewing',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_cooking',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_crafting',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_crushing',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_deceptionmagic',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_destructionmagic',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_foolery',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_foraging',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_galvanismmagic',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_gambit',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_hand',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_healingmagic',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_history',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_hunting',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_intimidation',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_intuition',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_investigation',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_medicine',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_performance',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_persuasion',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_pistols',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_religion',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_rifles',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_ritualmagic',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_ropework',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_shotguns',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_slashingmelee',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_sneak',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_thievery',
            field=models.IntegerField(default=5),
        ),
        migrations.AlterField(
            model_name='character',
            name='sk_utilitymagic',
            field=models.IntegerField(default=5),
        ),
    ]
