from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, update_session_auth_hash, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse, Http404
from Long.forms import ProvinceAdd
from django.views import View
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.models import User
from Long.models import Province, Bank, Branch
from Hoang.models import Customer, Card, Account
from django.contrib.auth.base_user import BaseUserManager
import datetime
from datetime import timedelta
import random
import string
# Create your views here.


def Home(request):
    return render(request, 'Long/index.html', {})

#dang ky nguoi dung
def signup(request):
    # if request.method == 'POST':
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data.get('Username')
    #         raw_password = form.cleaned_data.get('PassWord')
    #         user = authenticate(username=username, password=raw_password)
    #         login(request, user)
    #         return redirect('home')
    # else:
    #     form = UserCreationForm()
    # return render(request, 'Long/login.html', {'form': form})
    pass


def home_view(request):
    return render(request, 'Long/success_login.html', {})


class LoginAdmin(View):
    def get(self, request):
        return render(request, 'Long/login.html', {})

    def post(self, request):
        admin_user = request.POST.get('username')
        pass_word = request.POST.get('password')
        my_admin = authenticate(username=admin_user, password=pass_word)
        if my_admin is None:
            return HttpResponse("Sorry")
        else:
            login(request, my_admin)
            return render(request, 'Long/success_login.html', {'admin': admin_user})


def change_password_admin(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            current = User.objects.get(username=request.user)
            return HttpResponse('Tai khoan {} da thay doi mat khau thanh cong'.format(current.username))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'Long/change_password.html', {
        'form': form
    })


def logout_admin(request):
    logout(request)
    return redirect('Long:login')


class FindProvince(View):
    def get(self, request):
        return render(request, 'Long/find_province.html', {})

    def post(self, request):
        if request.method == 'POST':
           try:
               province_id = request.POST.get('province_id')
               object_province = Province.objects.get(province_id=province_id)
               return render(request, 'Long/result_province_find.html', {'province_object': object_province})
           except ValueError as e:
               return Http404('Can not find Province ID have {}'.format(e))
        else:
            return HttpResponse('It is not Post method')


class AddProvince(View):
    def get(self, request):
        form_province = ProvinceAdd()
        return render(request, 'Long/add_new_province.html', {'form': form_province})

    def post(self, request):
        if request.method == 'POST':
            form_province = ProvinceAdd(request.POST)
            if form_province.is_valid():
                form_province.save()
                return HttpResponse("Success")
            else:
                return HttpResponse("This form is not validate")
        else:
            return HttpResponse("It is not a method POST")


class FindBranch(View):
    def get(self, request):
        object_bank = Bank.objects.all()
        object_province = Province.objects.all()
        context = {
            'object_bank': object_bank,
            'object_province': object_province,
        }
        return render(request, 'Long/find_branch.html', context)

    def post(self, request):
        if request.method == 'POST':
            bank_id = request.POST['BankID']
            province_id = request.POST['ProvinceID']
            result_branch = Branch.objects.filter(bank_id=bank_id, province_id=province_id)
            return render(request, 'Long/result_branch_find.html', {'result': result_branch})
        else:
            return HttpResponse('click di dcm')


def searching(request):
    if request.method == 'GET':
        querry = request.GET.get('Search')

    else:
        return HttpResponse('hahaa')


def open_new_card(request):
    if request.method == 'POST':
        id_account = request.POST['id_account']
        account = Account.objects.filter(account_no=id_account).first()
        customer_name_input = request.POST['customer_name']
        try:
            if Account.objects.filter(customer_id__full_name__iexact=customer_name_input):
                max_card_number = 16
                card_no = random.randint(10**(max_card_number - 1), (10**max_card_number) - 1)
                create_date = datetime.datetime.today()
                end_date = create_date + timedelta(3650)
                card_type = request.POST['card_type']
                status = 1
                Card.objects.create(card_no=card_no,
                                    pin=BaseUserManager().make_random_password(6, string.digits),
                                    create_date=create_date, end_date=end_date,
                                    card_type=card_type,
                                    status=status,
                                    account_no=account)
                return HttpResponse('You have create new card with ID card {}'.format(card_no))
            else:
                messages.error('Check your name again!')
                return render(request, 'Long/add_new_province.html', {})
        except:
             return HttpResponse('Dont have this ID account {}'.format(id_account))
    else:
        return render(request, 'Long/open_new_card.html', {})
