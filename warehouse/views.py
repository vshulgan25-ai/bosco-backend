import random
from decimal import Decimal
from django.http import HttpResponse
from .models import Product


def products_view(request):
    products = Product.objects.all()
    rows = ""
    for p in products:
        rows += (
            "<tr>"
            f"<td>{p.id}</td>"
            f"<td>{p.product_name}</td>"
            f"<td>{p.brand}</td>"
            f"<td>{p.category}</td>"
            f"<td>{p.volume_ml}</td>"
            f"<td>{p.price}</td>"
            "</tr>"
        )
    html = f"""
    <!DOCTYPE html>
    <html lang="uk">
    <head>
        <meta charset="UTF-8">
        <title>Склад косметики</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 30px; }}
            table {{ border-collapse: collapse; width: 100%; }}
            th, td {{ border: 1px solid #999; padding: 8px; text-align: left; }}
            th {{ background: #f0f0f0; }}
        </style>
    </head>
    <body>
        <h1>Список косметики на складі</h1>
        <p>Всього записів: {products.count()}</p>
        <table>
            <tr>
                <th>ID</th><th>Назва</th><th>Бренд</th>
                <th>Категорія</th><th>Об'єм (мл)</th><th>Ціна</th>
            </tr>
            {rows}
        </table>
    </body>
    </html>
    """
    return HttpResponse(html)


def replenish_view(request, count):
    names = ["Шампунь", "Крем", "Парфум", "Туш", "Помада",
             "Гель для душу", "Лак", "Тонік", "Бальзам", "Скраб"]
    brands = ["Nivea", "L'Oreal", "Chanel", "Maybelline", "MAC",
              "Dove", "OPI", "Garnier", "Carmex", "The Body Shop"]
    categories = ["Догляд за волоссям", "Догляд за обличчям", "Парфумерія",
                  "Макіяж", "Манікюр", "Догляд за тілом", "Догляд за губами"]

    for _ in range(count):
        Product.objects.create(
            product_name=random.choice(names),
            brand=random.choice(brands),
            category=random.choice(categories),
            volume_ml=random.randint(5, 500),
            price=Decimal(random.randint(50, 3000)),
        )

    return HttpResponse(f"Додано {count} нових записів")