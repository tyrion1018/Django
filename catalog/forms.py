from django import forms
from .models import Person, City


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'birthdate', 'country', 'city')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.all()


class CityForm(forms.Form):
    cities = (
        ('Taipei', 'Taipei'),
        ('NewTaipei', 'NewTaipei'),
        ('TaiChung', 'TaiChung')
    )
    name = forms.ChoiceField(widget=forms.Select(),
                             choices=cities,
                             initial=cities[0]
                             )
