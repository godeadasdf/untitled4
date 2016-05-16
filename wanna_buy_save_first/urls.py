from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<item_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^login/$', views.login, name='login'),
    url(r'^home/(?P<user_id>[0-9]+)/$', views.home, name='home'),
]
