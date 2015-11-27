from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^friends/get/(?P<firstName>(.*))/$', views.get_friends,
        name='add_friends'),
    url(r'^friends/add/$', views.add_friends,name='add_friends'),
    url(r'^friends/delete/(?P<firstName>(.*))/$', views.delete_friends,
        name='delete_friends'),
]