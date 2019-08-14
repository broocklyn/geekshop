from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'page_title': 'админка/пользователи',

    }
    return render(request, 'adminapp/index.html', context)