from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.base, name='base'),
    url(r'^friends/get/(?P<friend_count>(.*))/$', views.get_friends,
        name='add_friends'),
    url(r'^friends/add/$', views.add_friends,name='add_friends'),
]