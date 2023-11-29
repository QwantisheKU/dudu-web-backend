from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView, DeleteView

from todo.models import Item
from todo_web.forms import CreateItemForm, UpdateItemForm


class ItemsListView(ListView):
    template_name = 'todo_web/all_items.html'

    def get_queryset(self):
        return Item.objects.filter(user_id=self.request.user.id)


class ItemUpdateView(UpdateView):
    model = Item
    form_class = UpdateItemForm
    template_name = 'todo_web/item_detail.html'

    def get_success_url(self):
        return reverse_lazy('items:item_detail', args=(self.object.id,))


class ItemCreateView(CreateView):
    model = Item
    form_class = CreateItemForm
    template_name = 'todo_web/create_item.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('items:all_items')


class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'todo_web/delete_item.html'

    def get_success_url(self):
        return reverse_lazy('items:all_items')