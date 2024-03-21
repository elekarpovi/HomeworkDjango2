from django.contrib import admin
from .models import User, Product, Order


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'date_registered']
    list_filter = ['name', 'date_registered']
    search_fields = ['name', 'email']
    search_help_text = 'Поиск по полям Имя(Name) и Email'
    list_editable = ['phone']

    readonly_fields = ['email']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'amount', 'date_added']
    list_filter = ['name', 'date_added']
    search_fields = ['name', 'description']
    search_help_text = 'Поиск по полям Имя(Name) и Описание(Description)'
    list_editable = ['amount']

    readonly_fields = ['photo']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'total_price', 'date_ordered']
    list_filter = ['customer', 'date_ordered']
    search_fields = ['customer']
    search_help_text = 'Поиск по полю Покупатель(customer)'
