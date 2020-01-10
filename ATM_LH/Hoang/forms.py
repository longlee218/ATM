from django import forms
from django.forms import inlineformset_factory

from .models import Customer, Account


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['full_name', 'card_type', 'card_no', 'gender', 'birthday',
                  'phone_number', 'email', 'address', 'branch_id', ]

