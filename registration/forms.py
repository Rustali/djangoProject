from django import forms
from .models import *


class RegistForm(forms.ModelForm):
    class Meta:
        model = RegFields
        fields = ['cat', 'email', 'name', 'inn', 'city', 'street', 'house', 'office', 'phone', 'site', 'store',
                  'regional_store', 'federal_store', 'online_store', 'car_service', 'other']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'input'}),
            'name': forms.TextInput(attrs={'class': 'input'}),
            'inn': forms.NumberInput(attrs={'class': 'input'}),
            'city': forms.TextInput(attrs={'class': 'input'}),
            'street': forms.TextInput(attrs={'class': 'input'}),
            'house': forms.TextInput(attrs={'class': 'input'}),
            'office': forms.TextInput(attrs={'class': 'input'}),
            'phone': forms.NumberInput(attrs={'class': 'input'}),
            'site': forms.TextInput(attrs={'class': 'input'}),
            'other': forms.TextInput(attrs={'class': 'input'}),
        }
