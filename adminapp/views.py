from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse

from adminapp.forms import ShopUserAdminCreateForm, ShopUserAdminUpdateForm, ProductCategoryAdminUpdateForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory


@user_passes_test(lambda x: x.is_superuser)
def index(request):
    object_list = ShopUser.objects.all()

    context = {
        'page_title': 'админка/пользователи',
        'object_list': object_list,

    }
    return render(request, 'adminapp/index.html', context)

@user_passes_test(lambda x: x.is_superuser)
def shopuser_create(request):
    if request.method == 'POST':
        form = ShopUserAdminCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:index'))
    else:
        form = ShopUserAdminCreateForm()

    content = {
        'title': 'админка/новый пользователь',
        'form': form
    }

    return render(request, 'adminapp/shopuser_update.html', content)



@user_passes_test(lambda x: x.is_superuser)
def shopuser_update(request, pk):
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        form = ShopUserAdminUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:index'))
    else:
        form = ShopUserAdminUpdateForm(instance=user)

    content = {
        'title': 'админка/редактирование пользователя',
        'form': form
    }

    return render(request, 'adminapp/shopuser_update.html', content)

@user_passes_test(lambda x: x.is_superuser)
def shopuser_delete(request, pk):
    # get_object_or_404(ShopUser, pk=pk).delete()
    user = get_object_or_404(ShopUser, pk=pk)
    if request.method == 'POST':
        user.is_active = False
        user.save()
        return HttpResponseRedirect(reverse('myadmin:index'))
    elif request.method == 'GET':
        context = {
            'page_title': 'админка/удаление пользователя',
            'object': user,
        }
        return render(request, 'adminapp/shopuser_delete.html', context)

def productcategory_list(request):
    object_list = ProductCategory.objects.all()
    context = {
        'title': 'админка/категории',
        'object_list': object_list
    }
    return render(request, 'adminapp/productcategory_list.html', context)


@user_passes_test(lambda x: x.is_superuser)
def productcategory_create(request):
    if request.method == 'POST':
        form = ProductCategoryAdminUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:productcategory_list'))
    else:
        form = ProductCategoryAdminUpdateForm()

    context = {
        'title': 'админка/новая категория товара',
        'form': form
    }

    return render(request, 'adminapp/productcategory_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def productcategory_update(request, pk):
    productcategory = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        form = ProductCategoryAdminUpdateForm(request.POST, request.FILES, instance=productcategory)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:productcategory_list'))
    else:
        form = ProductCategoryAdminUpdateForm(instance=productcategory)

    context = {
        'title': 'админка/редактирование категории товара',
        'form': form
    }

    return render(request, 'adminapp/productcategory_update.html', context)


@user_passes_test(lambda x: x.is_superuser)
def productcategory_delete(request, pk):
    productcategory = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        productcategory.is_active = False
        productcategory.save()
        return HttpResponseRedirect(reverse('myadmin:productcategory_list'))
    elif request.method == 'GET':
        context = {
            'title': 'админка/удаление категории',
            'object': productcategory,
        }
        return render(request, 'adminapp/productcategory_delete.html', context)