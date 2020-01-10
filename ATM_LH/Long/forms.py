from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Long.models import Province

# class SignUp(forms.ModelForm):
#     class Meta:
#         model = Customer
#         fields = ('branch_id', 'full_name', 'birthday', 'gender', 'hometown', 'phone_number',
#                   'email', 'card_type', 'card_no',)


class ProvinceAdd(forms.ModelForm):
    class Meta:
        model = Province
        fields = ('province_id', 'province_name',)
