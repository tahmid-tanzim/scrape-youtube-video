from django.core.management.base import BaseCommand

from ...tasks import start_background_task

class Command(BaseCommand):
    help = 'run background task'

    def handle(self, *args, **kwargs):
        start_background_task()