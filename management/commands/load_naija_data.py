from django.core.management import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Loads Nigeria's geographical data in order: zones → states → LGAs → wards"

    def handle(self, *args, **options):
        fixtures = [
            'zones.json',
            'states.json',
            'lgas.json',
            'wards.json'
        ]

        for fixture in fixtures:
            try:
                call_command('loaddata', fixture, verbosity=1)
                self.stdout.write(self.style.SUCCESS(
                    f"Successfully loaded {fixture}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(
                    f"Error loading {fixture}: {str(e)}"))
