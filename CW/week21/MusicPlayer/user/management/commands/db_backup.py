import os
import sys
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Backup the database'

    def add_arguments(self, parser):
        parser.add_argument('location', nargs='?', type=str, help='Location to save the backup file')

    def handle(self, *args, **options):
        db_engine = settings.DATABASES['default']['ENGINE']
        db_name = settings.DATABASES['default']['NAME']
        location = settings.BASE_DIR / (options['location'] or 'backup/')

        if db_engine == 'django.db.backends.sqlite3':

            os.makedirs(location, exist_ok=True)
            backup_file = os.path.join(location, f'{db_name}.db')

            shutil.copy(db_name, backup_file)
        elif db_engine == 'django.db.backends.postgresql':

            cmd = f'pg_dump -U {settings.DATABASES["default"]["USER"]} -d {db_name}  > {location}'
            os.system(cmd)

        elif db_engine == 'django.db.backends.mysql':
            cmd = f'mysqldump --user={settings.DATABASES["default"]["USER"]} --password={settings.DATABASES["default"]["PASSWORD"]} {db_name} > {location}'
            os.system(cmd)
        else:
            self.stdout.write(self.style.ERROR('Unsupported database engine'))

        self.stdout.write(self.style.SUCCESS(f'Successfully backed up the database to {location}'))
