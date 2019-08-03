from django.shortcuts import render


def login(request):
    return request(request, 'authapp/login.html')
