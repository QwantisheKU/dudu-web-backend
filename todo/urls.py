from django.urls import path, include
from .views import ItemView, ItemDetail, TagView, TagDetail, RegisterView
from rest_framework_simplejwt import views as jwt_views
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Dudu API",
      default_version="v1",
      description="Dudu API",
      terms_of_service="https://www.google.com/policies/terms/",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("auth/register/", RegisterView.as_view()),
    path("auth/token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("auth/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
    path("item/", ItemView.as_view()),
    path("item/<int:pk>/", ItemDetail.as_view()),
    path("tag/", TagView.as_view()),
    path("tag/<int:pk>/", TagDetail.as_view()),
    
    # Docs
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]