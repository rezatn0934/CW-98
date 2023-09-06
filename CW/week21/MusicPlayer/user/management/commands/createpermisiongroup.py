from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group


class Command(BaseCommand):
    help = 'Create a permission group for VIP users'

    def handle(self, *args, **options):
        group_name = 'VIP'
        group, created = Group.objects.get_or_create(name=group_name)

        if created:
            self.stdout.write(self.style.SUCCESS(f'Successfully created permission group: {group_name}'))
        else:
            self.stdout.write(self.style.NOTICE(f'Permission group "{group_name}" already exists'))
