from django.shortcuts import render

# Create your views here.

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
            'e-mail': 'info@geekshop.ru',
            'address': 'В пределах МКАД'
        },
        {
            'city': 'Санкт-Петербург',
            'phone': '+7-812-327-20-25',
            'e-mail': 'info@spb.geekshop.ru',
            'address': 'В пределах КАД'
        },
        {
            'city': 'Краснодар',
            'phone': '+7-831-188-13-46',
            'e-mail': 'info@krd.geekshop.ru',
            'address': 'В пределах края'
        }

    ]
    context = {
        'page_title': 'Контакты',
        'locations': 'locations',
    }
    return render(request, 'mainapp/contact.html', context)

def products(request):
    context = {
        'page_title': 'Товары',
    }
    return render(request, 'mainapp/products.html', context)