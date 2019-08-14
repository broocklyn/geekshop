from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse

from adminapp.forms import ShopUserAdminCreateForm, ShopUserAdminUpdateForm
from authapp.models import ShopUser


def index(request):
    object_list = ShopUser.objects.all()

    context = {
        'page_title': 'админка/пользователи',
        'object_list': object_list,

    }
    return render(request, 'adminapp/index.html', context)

def shopuser_create(request):
    if request.method == 'POST':
        form = ShopUserAdminCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:index'))
    else:
        form = ShopUserAdminCreateForm()

    content = {
        'title': 'админка/новый пользователь',
        'form': form
    }

    return render(request, 'adminapp/shopuser_update.html', content)

def shopuser_update(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        form = ShopUserAdminUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('adminapp:index'))
    else:
        form = ShopUserAdminUpdateForm(instance=user)

    content = {
        'title': 'админка/редактирование пользователя',
        'form': form
    }

    return render(request, 'adminapp/shopuser_update.html', content)