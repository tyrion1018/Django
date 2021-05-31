
from django.conf.urls.static import static

from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from MyDjango import settings
from . import views

urlpatterns = [
    path(r'', views.HomeView.as_view(), name='home'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
