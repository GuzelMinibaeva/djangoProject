from django.urls import path

from . import views

urlpatterns = [
    path("", views.MovieView.as_view(), name='index'),
    path("filter/", views.FilterMoviesView.as_view(), name='filter'),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name='movie_detail'),
    path("accounts/registration/", views.RegistrationView.as_view(), name='registration'),
]
