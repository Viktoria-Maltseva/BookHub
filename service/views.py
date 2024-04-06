from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.shortcuts import redirect
from django.shortcuts import redirect
from django.urls import reverse
from books.models import Author, Genre
from django.shortcuts import get_object_or_404



@require_http_methods(['GET', 'POST'])
def index(request):
    authors = Author.objects.all()
    genres = Genre.objects.all().order_by('genre')
    return render(request, 'base_main.html', {'authors': authors, 'genres': genres})


@require_http_methods(['GET', 'POST'])
def show_info_genres(request, genre_id):
    genre_info = Genre.objects.get(id=genre_id)
    return render(request, 'genres.html', {'genre': genre_info})

@require_http_methods(['GET', 'POST'])
def author_show(request, author_id):
    author_info = get_object_or_404(Author, id=author_id)
    return render(request, 'author.html', {'author': author_info})

@require_http_methods(['GET', 'POST'])
def sign_in(request):
    return render(request, 'sign_in.html')

@require_http_methods(['GET', 'POST'])
def sign_up(request):
    return render(request, 'sign_up.html')