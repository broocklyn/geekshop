from django.shortcuts import render


def login(request):
    form = ShopUserLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'authapp/login.html', context)
