from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.localflavor.ro.forms import ROPhoneNumberField

from models import Person, GENDER_CHOICES, CERT_CHOICES
from widgets import NameWidget


def unique_email(value):
    'Check if email exist.'
    try:
        person = Person.objects.get(email=value)
        raise ValidationError(u'This email exist in db, choose another.')
    except Person.DoesNotExist:
        pass

class PersonForm(forms.ModelForm):
    #first_name = forms.CharField(required=True)
    #last_name = forms.CharField(required=True)
    name = forms.CharField(required=True, widget=NameWidget())
    email = forms.EmailField(required=True, validators=[unique_email])
    confirm_email = forms.EmailField(required=True)
    sex = forms.ChoiceField(widget=forms.RadioSelect(), choices=GENDER_CHOICES, required=True)
    certificate = forms.ChoiceField(widget=forms.RadioSelect(), choices=CERT_CHOICES, required=True)
    phone = ROPhoneNumberField(required=True)
     
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'sex', 'email', 'confirm_email',
                  'profession', 'specialty', 'certificate', 'phone')
        
    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs = {'class': 'field text medium'}
        self.fields['profession'].widget.attrs = {'class': 'field select medium'}
        self.fields['specialty'].widget.attrs = {'class': 'field select large'}
        
    def clean(self):
        email = self.cleaned_data.get('email')
        confirm_email = self.cleaned_data.get('confirm_email')
        if email and confirm_email and email != confirm_email:
            raise forms.ValidationError(u'Emails not the same!') 
        return self.cleaned_data


