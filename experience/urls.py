from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    # path(r'', views.HomeView.as_view(), name='home'),
]

urlpatterns += staticfiles_urlpatterns()