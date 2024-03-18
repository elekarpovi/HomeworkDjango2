from django.core.management.base import BaseCommand

from myapp.models import Product


class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = Product(name='Cream', description='Milk 20%', price=10, amount=10)
        product.save()
        self.stdout.write(f'{product}')