from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError

from .models import UserModel


class UserRegistrationForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput())
    password1 = forms.CharField(widget=forms.PasswordInput(), error_messages={'errors': 'Пароли не совпадают'})
    password2 = forms.CharField(widget=forms.PasswordInput(), error_messages={'error': 'Пароли не совпадают'})

    class Meta:
        model = UserModel
        fields = ('email', 'password1', 'password2')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError(
                'Пароли не совпадают',
                code="password_mismatch",
            )
        if len(password1) < 8:
            raise ValidationError(
                'Пароль должен быть больше 8 символов'
            )
        return password2

    def clean(self):
        email = self.cleaned_data.get('email')

        if UserModel.objects.filter(email=email):
            raise ValidationError(
                'Аккаунт с данной почтой уже зарегестрирован',
                code='email',
            )

        return self.cleaned_data


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(), required=False)
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if email is not None and password:
            self.user_cache = authenticate(
                self.request, username=email, password=password
            )
            if self.user_cache is None:
                raise ValidationError(
                    'Неверный пароль'
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get('email')

        user = UserModel.objects.filter(email=email)
        if not user:
            raise ValidationError(
                'Аккаунта с такой почтой не существует'
            )
        return email

    class Meta:
        model = UserModel
        fields = ('email', 'password')



