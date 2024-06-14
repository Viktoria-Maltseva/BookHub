from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from books.models import Author, Genre
from django.shortcuts import get_object_or_404



@require_http_methods(['GET', 'POST'])
def index(request):
    authors = Author.objects.all()
    genres = Genre.objects.all().order_by('genre')
    return render(request, 'index.html', {'authors': authors, 'genres': genres})


@require_http_methods(['GET', 'POST'])
def show_info_genres(request, genre_id):
    if Genre.objects.filter(id=genre_id):
        genre_info = Genre.objects.get(id=genre_id)
        return render(request, 'genres.html', {'genre': genre_info})
    return render(request, '404.html')

@require_http_methods(['GET', 'POST'])
def author_show(request, author_id):
    if Author.objects.filter(id=author_id):
        author_info = Author.objects.get(id=author_id)
        return render(request, 'author.html', {'author': author_info})
    return render(request, '404.html')

@require_http_methods(['GET', 'POST'])
def notshowauth(request, auth_str):
    return render(request, '404.html')