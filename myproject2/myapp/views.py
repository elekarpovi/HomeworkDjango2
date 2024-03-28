from django.utils import timezone
from django.shortcuts import render, get_object_or_404

from .forms import ProductForm
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
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = Product(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                price=form.cleaned_data['price'],
                amount=form.cleaned_data['amount'],
                photo=form.cleaned_data['photo']
            )
            product.save()
    else:
        form = ProductForm()
    products = Product.objects.all()
    context = {
        "title": "Продукты",
        "products": products,
        'form': form,
    }
    return render(request, 'myapp/product.html', context)


def index(request):
    return render(request, "myapp/index.html")