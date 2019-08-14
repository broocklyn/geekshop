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
