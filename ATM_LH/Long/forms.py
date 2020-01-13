# from django import forms
# from .models import Customer, Account
# from django.core.validators import RegexValidator
#
#
# class RegistrationForm(forms.ModelForm):
#     full_name = forms.CharField(widget=forms.TextInput(
#         attrs={'placeholder': 'Enter full name'}
#     ), required=True, max_length=30)
#     id_no = forms.CharField(widget=forms.TextInput(
#         attrs={'placeholder': 'ID number'}
#     ), required=True, max_length=15)
#     birthday = forms.DateField(widget=forms.DateInput(
#         attrs={'placeholder': 'Enter Birthday'}
#     ), required=True)
#     phone_number = forms.CharField(min_length=10, validators=[
#         RegexValidator(r'((09|03|07|08|05)+([0-9]{8})\b)', message="Số điện thoại không hợp lệ")],
#                                    widget=forms.TextInput(
#                                        attrs={'placeholder': 'Enter phone number'}
#                                    ), required=True, max_length=11)
#     email = forms.CharField(validators=[RegexValidator(r'^[a-z][a-z0-9_\.]{5,32}@[a-z0-9]{2,}(\.[a-z0-9]{2,4}){1,2}$',
#                                                        message="Email không hợp lệ")],
#                             widget=forms.EmailInput(
#                                 attrs={'placeholder': 'Enter email'}
#                             ), required=True, max_length=50)
#     address = forms.CharField(widget=forms.TextInput(
#         attrs={'placeholder': 'Enter address'}
#     ), required=True, max_length=11)
#
#     class Meta:
#         model = Customer
#         fields = ['full_name', 'id_type', 'id_no', 'gender', 'birthday', 'phone_number', 'email', 'address',
#                   'branch_id']
#
#     def clean_card_no(self):
#         card_number = self.cleaned_data['id_no']
#         if card_number.isdigit():
#             try:
#                 match = Customer.objects.get(card_no=card_number)
#             except:
#                 return self.cleaned_data['id_no']
#             raise forms.ValidationError("Số giấy tờ đã tồn tại")
#         else:
#             raise forms.ValidationError("Số giấy tờ không hợp lệ")
#
#     def clean_phone_number(self):
#         sdt = self.cleaned_data['phone_number']
#         try:
#             match = Customer.objects.get(phone_number=sdt)
#         except:
#             return self.cleaned_data['phone_number']
#         raise forms.ValidationError("Số điện thoại đã tồn tại")
#
#     def clean_email(self):
#         email1 = self.cleaned_data['email']
#         try:
#             match = Customer.objects.get(email=email1)
#         except:
#             return self.cleaned_data['email']
#         raise forms.ValidationError("Email đã tồn tại")
#
#