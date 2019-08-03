from django.contrib.auth.forms import AuthenticationForm


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')
