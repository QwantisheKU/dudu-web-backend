from django.urls import path
from django.contrib.auth.decorators import login_required

from todo_web.views import ItemsListView, ItemUpdateView, ItemCreateView, ItemDeleteView

app_name = 'items'

urlpatterns = [
    path('all/', login_required(ItemsListView.as_view()), name='all_items'),
    path('item/<int:pk>/', login_required(ItemUpdateView.as_view()), name='item_detail'),
    path('create/', login_required(ItemCreateView.as_view()), name='item_create'),
    path('delete/<int:pk>/', login_required(ItemDeleteView.as_view()), name='item_delete'),
]
