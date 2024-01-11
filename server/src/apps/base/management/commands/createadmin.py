from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        # The magic line
        if User.objects.count() == 0:
            User.objects.create_user(
                username="careproadmin",
                email="carepro@gmail.com",
                password="12345",
                is_staff=True,
                is_active=True,
                is_superuser=True,
            )
            print("Admin created")
