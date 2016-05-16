from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item, User

app_name = 'wanna_buy_save_first/'


def index(request):
    items = Item.objects.all()
    context = {'items': items}
    return render(request, app_name + 'index.html', context)


def detail(request, item_id):
    if not request.session.get('user', False):
        return render(request, app_name + 'login.html')
    item = Item.objects.get(pk=item_id)
    context = {'item': item}
    return render(request, app_name + 'detail.html', context)


def login(request):
    try:
        m = User.objects.get(name=request.POST['username'])
    except:
        return render(request, app_name + 'login.html')
    else:
        if m.password == request.POST['password']:
            request.session['user'] = m.id
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            return HttpResponse("Your name and password didn't match")


def home(request, user_id):
    user = User.objects.get(id=user_id)
    context = {'user': user}
    if not request.session.get('user', False):
        return render(request, app_name + 'login.html')
    else:
        if int(request.session['user']) == int(user_id):
            context['session'] = request.session['user']
            context['req'] = user_id
            context['belong'] = 'me'
            return render(request, app_name + 'home.html', context)
        else:
            context['session'] = request.session['user']
            context['req'] = user_id
            context['belong'] = 'other'
            return render(request, app_name + 'home.html', context)
