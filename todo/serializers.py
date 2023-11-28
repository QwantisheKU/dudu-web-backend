from rest_framework import serializers
from .models import Item, Tag
from users.models import UserModel

class ItemSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    tag_id = serializers.IntegerField(required=False)
    class Meta:
        model = Item
        fields = ['id', 'title', 'description', 'deadline', 'priority', 'is_done', 'tag_id', 'user']

class TagSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Tag
        fields = ['id', 'name', 'user']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['id','email','password']
        extra_kwargs = {
            'password': {'write_only': True},
        }
    def create(self, validated_data):
        user = UserModel.objects.create_user(email = validated_data['email'], password = validated_data['password'])
        return user
