from .models import *
from django.contrib import admin

# Register your models here.
admin.site.register([Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews])