from django.views.generic import ListView, CreateView
from .models import BasketItem


class BasketItemsList(ListView):
    context_object_name = 'items'
    model = BasketItem
    template_name = 'basket/basket.html'


class CreateBasketItem(CreateView):
    model = BasketItem
    success_url = 'basket'
