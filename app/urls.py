from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.views.generic import RedirectView
from . import views

app_name = "app"

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.upload_file, name='upload'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)