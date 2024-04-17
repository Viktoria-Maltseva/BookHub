from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()
    photo = models.ImageField(upload_to='authors/', null=True, blank=True)

class Genre(models.Model):
    genre = models.CharField(max_length=255)
    body = models.TextField()

class Book(models.Model):
    name = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)