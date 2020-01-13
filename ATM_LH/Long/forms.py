from django import forms
from .models import Province


class ProvinceAdd(forms.ModelForm):
    class Meta:
        model = Province
        fields = ['province_id', 'province_name']
