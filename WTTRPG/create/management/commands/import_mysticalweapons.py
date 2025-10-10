import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from create.models import MysticalWeapon

class Command(BaseCommand):
    help = "Import weapon data from Weapon.csv"

    def handle(self, *args, **kwargs):
        csv_path = os.path.join(settings.BASE_DIR, 'create', 'MysticalWeapons.csv')

        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                MysticalWeapon.objects.update_or_create(
                    MysticalWeaponName = row['MysticalWeaponName'],
                    DamageType = row['DamageType'],
                    ActionCost = row['ActionCost'],
                    Range = row['Range'],
                    Damage = row['Damage'],
                    ExtraEffect = row['ExtraEffect']
                )

        self.stdout.write(self.style.SUCCESS('✅ Mystical Weapon data imported successfully.'))
