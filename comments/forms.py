from django.forms import ModelForm
from account.models import Comments
from django import forms

class CommentForm(ModelForm):
    title = forms.CharField(label='Заголовок')
    body = forms.CharField(label='Отзыв')
    class Meta:
        model = Comments
        fields = ['title', 'body']