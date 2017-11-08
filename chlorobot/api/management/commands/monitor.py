from django.core.management.base import BaseCommand, CommandError
from sensors import helper

class Command(BaseCommand):

	help = 'I monitor all the sensors, I run alongside the ASGI server'

	def handle(self, *args, **options):

        self.stdout.write(self.style.SUCCESS("It works"))
