from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import User, Product, Order
import datetime


def user_products(request, user_id, days):
    user = get_object_or_404(User, pk=user_id)
    orders = Order.objects.filter(customer=user, date_ordered__gte=timezone.now() - datetime.timedelta(days=days))
    products = set()

    for order in orders:
        products.update(order.products.all())

    context = {'user': user, 'days': days, 'products': products}
    return render(request, 'myapp/user_products.html', context)


def product(request):
    product = Product()
        
    
    context = {
        "title": "Продукты",
    }
    return render(request, 'myapp/product.html', context)
