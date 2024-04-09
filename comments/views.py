from django.shortcuts import render
from django.views import View
from .forms import CommentForm
from books.models import Book
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib import messages
from account.models import Comments

# Create your views here.
class CommentFormCreateView(View):

    def get(self, request, *args, **kwargs):
        form = CommentForm()
        book_id = kwargs['book_id']
        return render(request, 'comments/create.html', {'form': form, 'book_id': book_id})

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            book_id = self.kwargs.get('book_id')  # Получаем book_id из URL
            user_id = request.user.id
            if Comments.objects.filter(book_id=book_id, user_id=user_id).exists():
                messages.error(request, 'Вы уже оставили отзыв для этой книги')
                return redirect('show_book', id=book_id)
            book = Book.objects.get(id=book_id)  # Получаем объект книги
            comment = form.save(commit=False)
            comment.book = book  # Связываем комментарий с книгой
            comment.user_id = user_id
            comment.save()
            return redirect('show_book', id=book_id)
        messages.error(request, 'Произошла ошибка. Пожалуйста, попробуйте еще раз.')
        return render(request, 'comments/create.html', {'form': form})


class CommentFormEditView(View):

    def get(self, request, *args, **kwargs):
        comment_id = kwargs.get('comment_id')
        comment = Comments.objects.get(id=comment_id)
        form = CommentForm(instance=comment)
        return render(request, 'comments/update.html', {'form': form, 'comment_id':comment_id})

    def post(self, request, *args, **kwargs):
        comment_id = kwargs.get('comment_id')
        comment = Comments.objects.get(id=comment_id)
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

        return render(request, 'articles/update.html', {'form': form, 'comment_id':comment_id})


class CommentFormDeleteView(View):

    def post(self, request, *args, **kwargs):
        comment_id = kwargs.get('comment_id')
        comment = Comments.objects.get(id=comment_id)
        if comment:
            comment.delete()
        return redirect('dashboard')