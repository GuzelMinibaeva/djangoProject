from django.db import models
from django.contrib.auth.models import User, AnonymousUser
from movies.models import Movie


class BasketItem(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=AnonymousUser.id)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.movie.title}'

    class Meta:
        verbose_name = 'Фильм в корзине'
        verbose_name_plural = 'Фильмы в корзине'
