from django.core.management.base import BaseCommand

from myapp.models import User


class Command(BaseCommand):
    help = "Create user."

    def handle(self, *args, **kwargs):
        user = User(name='Kate', email='kate@example.com', phone='+375291000000', address='Minsk')
        user.save()
        self.stdout.write(f'{user}')