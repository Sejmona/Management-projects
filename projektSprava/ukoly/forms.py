from django import forms
from .models import Ukol

class UkolForm(forms.ModelForm):
    class Meta:
        model = Ukol
        fields = ['nazev', 'popis', 'datum_ukonceni', 'dokoncen']
