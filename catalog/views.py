from django.shortcuts import render
from django.template.loader import get_template
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Person, City, Country
from django.views import View
from .forms import CityForm


class PersonListView(ListView):
    model = Person
    context_object_name = 'people'


class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('person_changelist')


class PersonUpdateView(UpdateView):
    model = Person
    fields = ('name', 'birthdate', 'country', 'city')
    success_url = reverse_lazy('person_changelist')


class City(View):

    def get(self, request, *args, **kwargs):
        cities = CityForm()
        return render(request, "catalog/city_list.html", {'cities': cities})

    def post(self, request):
        select_form = CityForm(request.POST)
        if select_form.is_valid():
            get_value = request.POST.get('city', "")  # 这里可以取到下拉表单中的值
            # 接下来就是保存数值与其他逻辑了

        else:
            # 表单验证未通过的逻辑,多半要重新填写或直接给个404
            pass