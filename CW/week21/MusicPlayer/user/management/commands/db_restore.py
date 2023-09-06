import os
import shutil
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = 'Restore the database'

    def add_arguments(self, parser):
        parser.add_argument('location', nargs='?', type=str, help='Location of the backup file')

    def handle(self, *args, **options):
        db_engine = settings.DATABASES['default']['ENGINE']
        db_name = settings.DATABASES['default']['NAME']
        location = options['location'] or 'backup/'

        if db_engine == 'django.db.backends.sqlite3':
            backup_file = os.path.join(location, f'{db_name}.db')
            if os.path.isfile(backup_file):
                shutil.copyfile(backup_file, db_name)

                self.stdout.write(self.style.SUCCESS(f'Successfully restored the database from {backup_file}'))
            else:
                self.stdout.write(self.style.ERROR(f'Backup file {backup_file} does not exist'))

        elif db_engine == 'django.db.backends.postgresql':
            cmd = f'psql -U {settings.DATABASES["default"]["USER"]} -d {db_name} -f {location}'
            os.system(cmd)
            self.stdout.write(self.style.SUCCESS(f'Successfully restored the database from {location}'))

        elif db_engine == 'django.db.backends.mysql':
            cmd = f'mysql --user={settings.DATABASES["default"]["USER"]} --password={settings.DATABASES["default"]["PASSWORD"]} {db_name} < {location}'
            os.system(cmd)
            self.stdout.write(self.style.SUCCESS(f'Successfully restored the database from {location}'))
        else:
            self.stdout.write(self.style.ERROR('Unsupported database engine'))