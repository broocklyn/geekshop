from django.shortcuts import render

from authapp.forms import ShopUserLoginForm


def login(request):
    if request.method == 'POST':
        form = ShopUserLoginForm()
    else:
        form = ShopUserLoginForm(data=request.POST)
    form = ShopUserLoginForm()
    print(request.POST)
    context = {
        'form': form,
    }
    return render(request, 'authapp/login.html', context)
