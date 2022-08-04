

from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    text = forms.CharField(max_length = 250, min_length = 10)

    class Meta:
        model = Contact
        fields = '__all__'
