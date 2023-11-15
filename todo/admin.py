from django.contrib import admin
from todo.models import Item, Tag

admin.site.register(Item)
admin.site.register(Tag)