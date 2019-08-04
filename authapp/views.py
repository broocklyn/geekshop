from django.shortcuts import render

from authapp.forms import ShopUserLoginForm


def login(request):
    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            print('OK')
    else:
        form = ShopUserLoginForm()

    context = {
        'form': form,
    }
    return render(request, 'authapp/login.html', context)
