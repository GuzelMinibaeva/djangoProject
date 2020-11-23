from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Movie, Genre
# Create your views here.


class GenreYear:
    """Жанры и года выхода фильмов"""
    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.filter(draft=False).values("year")


class MovieView(GenreYear, ListView):
    """Cписок фильмов"""
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    # template_name = "movies/movie_list.html"


class MovieDetailView(GenreYear, DetailView):
    """Полное описание фильмов"""
    model = Movie
    slug_field = "url"


class FilterMoviesView(GenreYear, ListView):
    """Фильтр фильмов"""
    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(year__in=self.request.GET.getlist("year")) &
            Q(genres__in=self.request.GET.getlist("genre"))
        )
        return queryset


class RegistrationView(CreateView):
   model = User
   template_name = 'movies/registration.html'
   form_class = UserCreationForm
   success_url = reverse_lazy('login')
