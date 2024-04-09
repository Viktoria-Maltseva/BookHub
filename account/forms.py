from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

# class CommentFormEditView(View):
#     def get(self, request, *args, **kwargs):
#         comment_id = kwargs.get('id')
#         comment = Comments.objects.get(id=comment_id)
#         form = CommentForm(instance=comment)
#         return render(request, 'articles/update.html', {'form': form, 'article_id':article_id})
#     def post(self, request, *args, **kwargs):
#         comment_id = kwargs.get('id')
#         comment = Comments.objects.get(id=comment_id)
#         form = CommentForm(request.POST, instance=comment)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')

#         return render(request, 'comments/update.html', {'form': form, 'comment_id':comment_id})