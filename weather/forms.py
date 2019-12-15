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
        labels = {
            'email_address': "Email",
            'location': "Location"
        }

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs) # Call to ModelForm constructor
        self.fields['email_address'].widget.attrs['size'] = 39
        self.fields['location'].widget.attrs['size'] = 35
