from rest_framework import serializers
from .models import Item, Tag

# TODO: foreign keys in serializers
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'title', 'description', 'deadline', 'priority', 'is_done', 'tag_id', 'user_id']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'user_id']
