from django.urls import path
from . import views

urlpatterns = [
    path('', views.BasketItemsList.as_view(), name='basket'),
]
