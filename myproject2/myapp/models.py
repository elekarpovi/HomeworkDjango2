from django.db import models
from django.utils import timezone


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}, email: {self.email}, phone: {self.phone}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    amount = models.IntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='product_photos/', default='default_product.jpg')

    def __str__(self):
        return f'Product #{self.pk}: {self.name}, price: {self.price}, amount: {self.amount}'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        products = ', '.join([product.name for product in self.products.all()])
        return f'Order #{self.pk}: customer: {self.customer.name}, total_price: {self.total_price}, products: {products}'



