from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from adminapp.forms import ShopUserAdminCreateForm, ShopUserAdminUpdateForm, ProductCategoryAdminUpdateForm, \
    ProductAdminUpdateForm
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


# @user_passes_test(lambda x: x.is_superuser)
# def index(request):
#     object_list = ShopUser.objects.all()
#
#     context = {
#         'page_title': 'админка/пользователи',
#         'object_list': object_list,
#
#     }
#     return render(request, 'adminapp/shopuser_list.html', context)


class ShopUserListView(ListView):
    model = ShopUser
#    template_name = 'adminapp/shopuser_list.html'

    @method_decorator(user_passes_test(lambda x: x.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


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


# @user_passes_test(lambda x: x.is_superuser)
# def productcategory_create(request):
#     if request.method == 'POST':
#         form = ProductCategoryAdminUpdateForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('myadmin:productcategory_list'))
#     else:
#         form = ProductCategoryAdminUpdateForm()
#
#     context = {
#         'title': 'админка/новая категория товара',
#         'form': form
#     }
#
#     return render(request, 'adminapp/productcategory_update.html', context)

class ProductCategoryCreateView(CreateView):
    model = ProductCategory
    success_url = reverse_lazy('myadmin:productcategory_list')
    # fields = '__all__'
    form_class = ProductCategoryAdminUpdateForm


# @user_passes_test(lambda x: x.is_superuser)
# def productcategory_update(request, pk):
#     productcategory = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         form = ProductCategoryAdminUpdateForm(request.POST, request.FILES, instance=productcategory)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('myadmin:productcategory_list'))
#     else:
#         form = ProductCategoryAdminUpdateForm(instance=productcategory)
#
#     context = {
#         'title': 'админка/редактирование категории товара',
#         'form': form
#     }
#
#     return render(request, 'adminapp/productcategory_update.html', context)

class ProductCategoryUpdateView(UpdateView):
    model = ProductCategory
    success_url = reverse_lazy('myadmin:productcategory_list')
    form_class = ProductCategoryAdminUpdateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/редактирование категории товара'
        return context

# @user_passes_test(lambda x: x.is_superuser)
# def productcategory_delete(request, pk):
#     productcategory = get_object_or_404(ProductCategory, pk=pk)
#     if request.method == 'POST':
#         productcategory.is_active = False
#         productcategory.save()
#         return HttpResponseRedirect(reverse('myadmin:productcategory_list'))
#     elif request.method == 'GET':
#         context = {
#             'title': 'админка/удаление категории',
#             'object': productcategory,
#         }
#         return render(request, 'adminapp/productcategory_delete.html', context)

class ProductCategoryDeleteView(DeleteView):
    model = ProductCategory
    success_url = reverse_lazy('myadmin:productcategory_list')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

@user_passes_test(lambda x: x.is_superuser)
def productcategory_products(request, pk):
    productcategory = get_object_or_404(ProductCategory, pk=pk)
    content = {
        'title': 'админка/товары категории',
        'productcategory': productcategory,
        'object_list': productcategory.product_set.all()
    }

    return render(request, 'adminapp/product_list.html', content)


@user_passes_test(lambda x: x.is_superuser)
def product_create(request, pk):
    productcategory = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        form = ProductAdminUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:productcategory_products', kwargs={'pk': pk}))
    else:
        form = ProductAdminUpdateForm(initial={'category': productcategory})

    content = {
        'title': 'админка/новый товар',
        'form': form
    }

    return render(request, 'adminapp/product_update.html', content)


@user_passes_test(lambda x: x.is_superuser)
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductAdminUpdateForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('myadmin:productcategory_products',
                                                kwargs={'pk': product.category.pk}))
    else:
        form = ProductAdminUpdateForm(instance=product)

    content = {
        'title': 'админка/редактирование товара',
        'form': form,
        'object': product
    }

    return render(request, 'adminapp/product_update.html', content)


@user_passes_test(lambda x: x.is_superuser)
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.is_active = False
        product.save()
        return HttpResponseRedirect(reverse('myadmin:productcategory_products',
                                            kwargs={'pk': product.category.pk}))
    elif request.method == 'GET':
        context = {
            'title': 'админка/удаление товара',
            'object': product,
        }
        return render(request, 'adminapp/product_delete.html', context)


# @user_passes_test(lambda x: x.is_superuser)
# def product_read(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'title': 'админка/товар подробно',
#         'object': product
#     }
#
#     return render(request, 'adminapp/product_read.html', context)

class ProductDetailView(DetailView):
    model = Product