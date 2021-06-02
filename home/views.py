from django.shortcuts import render
from django.views import View
from .forms import HomeForm


class HomeView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "home/home.html")
