from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^friends/(?P<friend_count>(.*))/$', views.get_friends,
        name='add_friends'),
    url(r'^friends/add/$', views.add_friends,name='add_friends'),
]