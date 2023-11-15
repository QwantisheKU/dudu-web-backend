from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from .models import UserModel
from .forms import UserRegistrationForm


class UserRegistrationView(CreateView):
    model = UserModel
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:success')


class SuccessRegistrationView(TemplateView):
    template_name = 'users/success_page.html'
