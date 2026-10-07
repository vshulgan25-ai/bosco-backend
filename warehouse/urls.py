from django.urls import path
from . import views

urlpatterns = [
    path('products', views.products_view, name='products'),
    path('replenish/<int:count>', views.replenish_view, name='replenish'),
]