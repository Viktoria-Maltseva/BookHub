from django.forms import ModelForm
from account.models import Comments

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['title', 'body']