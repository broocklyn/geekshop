from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'page_title': 'Магазин1',
    }
    return render(request, 'mainapp/index.html', context)

def contact(request):
    return render(request, 'mainapp/contact.html')

def products(request):
    return render(request, 'mainapp/products.html')