import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from create.models import Spell

class Command(BaseCommand):
    help = "Import spell data from Spells.csv"

    def handle(self, *args, **kwargs):
        csv_path = os.path.join(settings.BASE_DIR, 'create', 'Spells.csv')

        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Spell.objects.update_or_create(
                    MagicSchool = row['MagicSchool'],
                    SpellDescription = row['SpellDescription'],
                    SpellName = row['SpellName'],
                    ActionCost = row['ActionCost'],
                    Range = row['Range'],
                    SpellEffect = row['SpellEffect']
                )

        self.stdout.write(self.style.SUCCESS('✅ Spell data imported successfully.'))
