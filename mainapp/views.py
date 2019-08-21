import random

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404

# Create your views here.
from mainapp.models import Product, ProductCategory


def get_products_menu():
    return ProductCategory.objects.all()


def get_basket(request):
    if request.user.is_authenticated:
        return request.user.basket.all().order_by('product__category')
    else:
        return []


def get_hot_product():
    return random.choice(Product.objects.all())


def same_products(hot_product):
    return hot_product.category.product_set.exclude(pk=hot_product.pk)


def index(request):
    context = {
        'page_title': 'Магазин',
        'basket': get_basket(request),

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
        'basket': get_basket(request),

    }
    return render(request, 'mainapp/contact.html', context)


def products(request):
    hot_product = get_hot_product()
    context = {
        'page_title': 'Товары',
        'products_menu': get_products_menu(),
        'hot_product': hot_product,
        'same_products': same_products(hot_product),
        'basket': get_basket(request),

    }
    return render(request, 'mainapp/products.html', context)


def category(request, pk, page=1):
    pk = int(pk)
    if pk == 0:
        category = {
            'pk': 0,
            'name': 'все'
        }
        category_products = Product.objects.all()
    else:
        category = get_object_or_404(ProductCategory, pk=pk)
        #   category = ProductCategory.objects.filter(pk=pk).first()
        #   category = ProductCategory.objects.get(pk=pk)
        category_products = category.product_set.all()
    #       category_products = Product.objects.filter(category=pk)

    paginator = Paginator(category_products, 2)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {
        'page_title': 'раздел каталога товаров',
        'products_menu': get_products_menu(),
        'category': category,
        'category_products': products_paginator,
        'basket': get_basket(request),

    }
    return render(request, 'mainapp/category_products.html', context)


def product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    context = {
        'page_title': 'страница подукта',
        'products_menu': get_products_menu(),
        'category': product.category,
        'object': product,
        'basket': get_basket(request),
    }
    return render(request, 'mainapp/product_page.html', context)
