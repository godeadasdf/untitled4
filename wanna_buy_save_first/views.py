from django.shortcuts import render
from .models import Item


def index(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'wanna_buy_save_first/index.html', context)


def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {'item': item}
    return render(request, 'wanna_buy_save_first/detail.html', context)
