from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Movie
# Create your views here.

class MovieView(ListView):
    """Cписок фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = "movies/movie_list.html"

class MovieDetailView(DetailView):
    """Полное описание фильмов"""
    model = Movie
    slug_field = "url"