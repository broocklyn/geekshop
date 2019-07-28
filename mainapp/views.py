from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'page_title': 'Магазин',
    }
    return render(request, 'mainapp/index.html', context)

def contact(request):
    context = {
        'page_title': 'Контакты',
    }
    return render(request, 'mainapp/contact.html', context)

def products(request):
    context = {
        'page_title': 'Товары',
    }
    return render(request, 'mainapp/products.html', context)