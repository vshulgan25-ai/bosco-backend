from django import template
from warehouse.models import Product

register = template.Library()


@register.filter
def uah(value):
    return f"{value} ₴"


@register.simple_tag
def product_count():
    return Product.objects.count()