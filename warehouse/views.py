from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product


def products_view(request):
    products = Product.objects.all()
    return render(request, 'warehouse/products.html', {'products': products})


def product_add(request):
    if request.method == 'POST':
        Product.objects.create(
            product_name=request.POST['product_name'],
            brand=request.POST['brand'],
            category=request.POST['category'],
            volume_ml=request.POST['volume_ml'],
            price=request.POST['price'],
        )
        messages.success(request, 'Товар додано')
        return redirect('products')

    return render(request, 'warehouse/product_form.html')