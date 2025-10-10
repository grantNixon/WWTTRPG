import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from create.models import Perk

class Command(BaseCommand):
    help = "Import weapon data from Weapon.csv"

    def handle(self, *args, **kwargs):
        csv_path = os.path.join(settings.BASE_DIR, 'create', 'perk_list.csv')

        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Perk.objects.update_or_create(
                    perkSkill = row['Skill'],
                    perkName = row['Perk'],
                    skillLevel = row['SkillLevel'],
                    description = row['PerkEffect']
                )

        self.stdout.write(self.style.SUCCESS('✅ Perk data imported successfully.'))
