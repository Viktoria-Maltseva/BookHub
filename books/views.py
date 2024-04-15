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
        book = get_object_or_404(Book, id=kwargs['id'])
        comments = Comments.objects.filter(book=kwargs['id'])
        return render(request, 'books/book.html', context={'book': book, 'comments': comments})

@require_http_methods(['GET', 'POST'])
def search_redirect(request):
    query = request.GET.get('term')
    if query:
        books = Book.objects.filter(Q(genre__genre__icontains=query) | Q(author__name__icontains=query) | Q(name__icontains=query))
        return render(request, 'search_results.html', {'books': books, 'query': query})
    else:
        return render(request, 'search_results.html', {'query': query})