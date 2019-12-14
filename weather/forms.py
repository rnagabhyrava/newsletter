from dal import autocomplete
from django import forms
from weather.models import Email, Location

class SignupForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ('email_address', 'location')
        widgets = {
            'location': autocomplete.ModelSelect2(url='weather:location-autocomplete')
        }
