from django.shortcuts import get_object_or_404, render
from django.views import View
from books.models import Book
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.db.models import Q
from account.models import Comments

# Create your views here.
class BookView(View):
    def get(self, request, *args, **kwargs): 
        if Book.objects.filter(id=kwargs['book_id']):
            book = Book.objects.get(id=kwargs['book_id'])
            comments = Comments.objects.filter(book=kwargs['book_id'])
            if request.user.is_authenticated:
                current_user_comment = comments.filter(user=request.user).first()
                if current_user_comment:
                    comments = [current_user_comment] + list(comments.exclude(id=current_user_comment.id))
                    request.session['comment_id'] = current_user_comment.id
            request.session['book_id'] = kwargs.pop('book_id')
            return render(request, 'books/book.html', context={'book': book, 'comments': comments})
        else:
            return render(request, '404.html')

@require_http_methods(['GET', 'POST'])
def search_redirect(request):
    query = request.GET.get('term')
    if query:
        books = Book.objects.filter(Q(genre__genre__icontains=query) | Q(author__name__icontains=query) | Q(name__icontains=query))
        return render(request, 'search_results.html', {'books': books, 'query': query})
    else:
        return render(request, 'search_results.html', {'query': query})
    

@require_http_methods(['GET', 'POST'])
def notbook(request, book_not):
    return render(request, '404.html')