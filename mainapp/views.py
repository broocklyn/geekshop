from django.shortcuts import render

# Create your views here.
from mainapp.models import Product, ProductCategory


def get_products_menu():
    return ProductCategory.objects.all()


def index(request):
    context = {
        'page_title': 'Магазин',
    }
    return render(request, 'mainapp/index.html', context)


def contact(request):
    locations = [
        {
            'city': 'Москва',
            'phone': '+7-495-468-20-35',
            'email': 'info@geekshop.ru',
            'address': 'В пределах МКАД'
        },
        {
            'city': 'Санкт-Петербург',
            'phone': '+7-812-327-20-25',
            'email': 'info@spb.geekshop.ru',
            'address': 'В пределах КАД'
        },
        {
            'city': 'Краснодар',
            'phone': '+7-831-188-13-46',
            'email': 'info@krd.geekshop.ru',
            'address': 'В пределах края'
        }

    ]
    context = {
        'page_title': 'Контакты',
        'locations': locations,
    }
    return render(request, 'mainapp/contact.html', context)


def products(request):
    same_products = Product.objects.all()

    context = {
        'page_title': 'Товары',
        'products_menu': get_products_menu(),
        'same_products': same_products,
    }
    return render(request, 'mainapp/products.html', context)


def category(request, pk):
    pk = int(pk)
    if pk == 0:
        category_products = Product.objects.all()
    else:
        category = ProductCategory.objects.filter(pk=pk).first()
        category_products = category.product_set.all()
#        category_products = Product.objects.filter(category=pk)
    context = {
        'page_title': 'Товары',
        'products_menu': get_products_menu(),
        'category_': category,
        'category_products': category_products,

    }
    return render(request, 'mainapp/products.html', context)
