from django import forms
from .widgets import AjaxInputWidget
from .models import City


class SearchTicket(forms.Form):
    default_value = ((None, '--------------'),)
    choices = default_value + tuple(((city.name, city.name) for city in City.objects.all()))

    departure_city = forms.CharField(widget=AjaxInputWidget(url='api/city_ajax',
                                     attrs={'class': 'inline right-margin'}),
                                     label='Город отбытия')
    arrival_city = forms.ChoiceField(choices=choices, label='Город прибытия')
    fly_date = forms.DateField(widget=forms.SelectDateWidget(), label='Дата вылета')

    class Meta(object):
        model = City
        exclude = ('id', 'name')
