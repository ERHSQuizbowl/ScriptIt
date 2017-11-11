from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url

import views as views

urlpatterns = [
    url(r'^$', views.main, name='reader'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)