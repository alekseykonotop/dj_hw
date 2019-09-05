from django import forms
from .models import Game


class GuessNumberForm(forms.Form):
    number = forms.IntegerField(label="Загаданное число")