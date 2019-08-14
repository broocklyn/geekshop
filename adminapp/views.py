from django.shortcuts import render

# Create your views here.
from authapp.models import ShopUser


def index(request):
    object_list = ShopUser.objects.all()

    context = {
        'page_title': 'админка/пользователи',
        'object_list': object_list,

    }
    return render(request, 'adminapp/index.html', context)