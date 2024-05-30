from django import forms
from django.forms.widgets import NumberInput
from .models import GeesModel
import datetime

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=10)


class CommentForm(forms.Form):
    Comment = forms.CharField(widget=forms.Textarea)


class Form_widget_attribute(forms.Form):
    Comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))

class EmailForm(forms.Form):
    Email = forms.EmailField()

class BoolField(forms.Form):
    Agree = forms.BooleanField()

class DatField(forms.Form):
    Date = forms.DateField()

class DateWithField(forms.Form):
    DatWithField = forms.DateField(widget=NumberInput(attrs={'type':'date'}))

BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
class DateWithSelect(forms.Form):
    DateWithSelect = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))

class Decimal(forms.Form):
    Value = forms.DecimalField()

class max(forms.Form):
    Message = forms.CharField(
        max_length=10,
    )

class LabelWith(forms.Form):
    email_address = forms.EmailField(
        label="Please Enter Your Email Address",
    )

class InitialValue(forms.Form):
    name = forms.CharField(max_length=20,label='First Name',initial='Your Name')

class InitialBoolean(forms.Form):
    Agree = forms.BooleanField(initial=True)

class InitialDate(forms.Form):
    Day = forms.DateField(initial=datetime.date.today,widget=NumberInput(attrs={'type':'date'}))

FAVORITE_COLORS_CHOICES = [
    ('blue','Blue'),
    ('green','Green'),
    ('black','Black'),
    ('red','Red'),
]

class MultipleChoice(forms.Form):
    favorite_color = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)


class MultipleChoiceRadio(forms.Form):
    radio = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES)


class GeeksForm(forms.ModelForm):
    class Meta:
        model = GeesModel
        fields = "__all__"