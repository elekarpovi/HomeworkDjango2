from django.urls import path
from . import views

urlpatterns = [
    path('hw/', views.hw, name='hw'),
]