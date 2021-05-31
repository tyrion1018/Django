from django.urls import include, path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path(r'', views.PersonListView.as_view(), name='person_changelist'),
    path(r'add/', views.City.as_view(), name='city_list'),
]

urlpatterns += staticfiles_urlpatterns()
