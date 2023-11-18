from django.urls import path, include
from .views import ItemView, ItemDetail, TagView, TagDetail, RegisterView
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path("auth/register/", RegisterView.as_view()),
    path("auth/token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("item/", ItemView.as_view()),
    path("item/<int:pk>/", ItemDetail.as_view()),
    path("tag/", TagView.as_view()),
    path("tag/<int:pk>/", TagDetail.as_view()),
]