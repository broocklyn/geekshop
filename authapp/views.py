from django.shortcuts import render


def login(request):
    context = {

    }
    return request(request, 'authapp/login.html', context)
