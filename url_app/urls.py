from django.conf.urls import url
from url_app import views


app_name = 'url_app'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<short>[\w\+]+)/$', views.redirect, name='redirect'),
]

