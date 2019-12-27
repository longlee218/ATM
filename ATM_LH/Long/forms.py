from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Hoang.models import Customer


class SignUp(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('branch_id', 'full_name', 'birthday', 'gender', 'hometown', 'phone_number',
                  'email', 'card_type', 'card_no',)
