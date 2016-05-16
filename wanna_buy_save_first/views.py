from django.shortcuts import render
from django.http import HttpResponse
from .models import Item, User


def index(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, 'wanna_buy_save_first/index.html', context)


def detail(request, item_id):
    if not request.session.get('user', False):
        return render(request, 'wanna_buy_save_first/login.html')
    item = Item.objects.get(pk=item_id)
    context = {'item': item}
    return render(request, 'wanna_buy_save_first/detail.html', context)


def login(request):
    m = User.objects.get(name=request.POST['username'])
    if m.password == request.POST['password']:
        request.session['user'] = m.id
        return HttpResponse("You're logged in")
    else:
        return HttpResponse("Your name and password didn't match")
