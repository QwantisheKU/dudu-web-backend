from django import forms

from todo.models import Item


class CreateItemForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Item
        fields = ('title', 'description', 'deadline', 'priority', 'is_done', 'tag')


class UpdateItemForm(forms.ModelForm):
    deadline = forms.DateTimeField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Item
        # fields = '__all__'
        fields = ('title', 'description', 'deadline', 'priority', 'is_done', 'tag')
