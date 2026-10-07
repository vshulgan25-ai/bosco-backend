from django.urls import path
from . import views

urlpatterns = [
    path('products', views.products_view, name='products'),
    path('products/add', views.product_add, name='product_add'),
]