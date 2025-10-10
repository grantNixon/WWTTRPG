import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from create.models import Clothing

class Command(BaseCommand):
    help = "Import tonic data from Tonics.csv"

    def handle(self, *args, **kwargs):
        csv_path = os.path.join(settings.BASE_DIR, 'create', 'Tonics.csv')

        with open(csv_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Clothing.objects.update_or_create(
                    TonicName = row['TonicName'],
                    TonicDescription = row['TonicDescription'],
                    TonicSize = row['ActonCost']
                )

        self.stdout.write(self.style.SUCCESS('✅ Clothing data imported successfully.'))
