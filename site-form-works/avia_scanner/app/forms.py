from django import forms
from .widgets import AjaxInputWidget
from django.urls import reverse_lazy
from .models import City


class SearchTicket(forms.Form):
    departure_city = forms.CharField(widget=AjaxInputWidget(url=reverse_lazy('cities_lookup'),
                                     attrs={'class': 'inline right-margin'}),
                                     label='Город отбытия')
    arrival_city = forms.ModelChoiceField(queryset=City.objects.all(), empty_label='---------',
                                          label='Город прибытия')
    fly_date = forms.DateField(widget=forms.SelectDateWidget, label='Дата вылета')

    class Meta(object):
        model = City
        exclude = ('id', 'name')
