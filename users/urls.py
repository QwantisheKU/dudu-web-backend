from django.urls import path

from users.views import UserRegistrationView, SuccessRegistrationView

app_name = 'users'

urlpatterns = [
    path("success/", SuccessRegistrationView.as_view(), name='success'),
    path("registration/", UserRegistrationView.as_view(), name='registration'),
]
