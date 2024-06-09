from django import forms 
from .models import musician

class musician_form(forms.ModelForm):
    class Meta:
        model = musician
        fields = "__all__"
        labels = {
            "FirstName": "First Name",
            "LastName": "Last Name",
            "PhoneNumber":"Phone Number",
            "InstrumentType":"Instrument Type"
        }