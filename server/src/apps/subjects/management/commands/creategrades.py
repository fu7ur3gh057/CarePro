from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from src.apps.subjects.models import Grade


class Command(BaseCommand):
    def handle(self, *args, **options):
        # The magic line
        if Grade.objects.count() == 0:
            for i in range(9, 12):
                Grade.objects.create(number=i)
            print("Grades have been created")
