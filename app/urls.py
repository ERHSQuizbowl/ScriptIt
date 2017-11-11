from django.conf.urls import include, url
from django.views.generic import RedirectView
from . import views

app_name = "app"

urlpatterns = [
    url(r'^$', views.index, name='index'),
]