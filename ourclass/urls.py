from django.conf.urls import url
from . import views

app_name = 'ourclass'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<user_name>[a-z]+)/$', views.personalpage, name='personalpage'),
]
