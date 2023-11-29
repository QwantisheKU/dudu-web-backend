from django.urls import path

from todo_web.views import ItemsListView, ItemUpdateView, ItemCreateView, ItemDeleteView

app_name = 'items'

urlpatterns = [
    path('all/', ItemsListView.as_view(), name='all_items'),
    path('item/<int:pk>/', ItemUpdateView.as_view(), name='item_detail'),
    path('create/', ItemCreateView.as_view(), name='item_create'),
    path('delete/<int:pk>/', ItemDeleteView.as_view(), name='item_delete'),
]
