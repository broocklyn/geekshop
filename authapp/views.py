from django.shortcuts import render
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings

from authapp.forms import ShopUserLoginForm, ShopUserUpdateForm, ShopUserProfileEditForm
from django.contrib import auth
from django.http import HttpResponseRedirect
from authapp.forms import ShopUserRegisterForm
from authapp.models import ShopUser
from django.db import transaction


def login(request):
    next = request.GET['next'] if 'next' in request.GET.keys() else None

    if request.method == 'POST':
        form = ShopUserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                next = request.POST['next'] if 'next' in request.POST.keys() else None
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index') if not next else next)
    else:
        form = ShopUserLoginForm()

    context = {
        'title': 'вход в систему',
        'form': form,
        'next': next,
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('main:index'))


def register(request):
    if request.method == 'POST':
        register_form = ShopUserRegisterForm(request.POST, request.FILES)

        if register_form.is_valid():
            user = register_form.save()
            if send_verify_mail(user):
                print('Отправлено')
                return HttpResponseRedirect(reverse('auth:login'))
            else:
                print('Ошибка отправки')
                return HttpResponseRedirect(reverse('auth:login'))
    else:
        register_form = ShopUserRegisterForm()

    content = {
        'title': 'регистрация в системе',
        'form': register_form
    }

    return render(request, 'authapp/register.html', content)

@transaction.atomic
def update(request):
    if request.method == 'POST':
        form = ShopUserUpdateForm(request.POST, request.FILES, instance=request.user)

        profile_form = ShopUserProfileEditForm(request.POST, instance=request.user.shopuserprofile)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:update'))
    else:
        form = ShopUserUpdateForm(instance=request.user)
        profile_form = ShopUserProfileEditForm(instance=request.user.shopuserprofile)

    context = {
        'title': 'редактирование',
        'form': form,
        'profile_form': profile_form

    }

    return render(request, 'authapp/update.html', context)

def send_verify_mail(user):
    verify_link = reverse('auth:verify', args=[user.email, user.activation_key])

    title = f"Подтверждение учетной записи {user.username}"
    message = (f"Для подтверждения учетной записи {user.username}"
                f"на портале {settings.DOMAIN_NAME} перейдите по "
                f"ссылке:\n{settings.DOMAIN_NAME}{verify_link}")

    return send_mail(title, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

def verify(request, email, activation_key):
    try:
        user = ShopUser.objects.get(email=email)
        if (user.activation_key == activation_key and not user.is_activation_key_expired()):
            user.is_active = True
            user.save()
            auth.login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return render(request, 'authapp/verification.html')
        else:
            print(f'Error activation user: {user}')
            return render(request, 'authapp/verification.html')
    except Exception as e:
        print(f'error activating user: {e.args}')
        return HttpResponseRedirect(reverse('main:index'))

