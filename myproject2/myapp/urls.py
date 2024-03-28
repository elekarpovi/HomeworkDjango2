from django.urls import path
from . import views
from .views import user_products, index

urlpatterns = [
    path('user/<int:user_id>/<int:days>', user_products, name='user_products'),
    path('product/', views.product, name='product'),
    path('', index, name='index'),
]