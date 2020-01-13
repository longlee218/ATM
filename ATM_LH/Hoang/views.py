from django.contrib import auth, messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.http import HttpResponse
import random
from datetime import timedelta
import datetime
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, SigninForm
from Hoang.models import Account, Customer
from django.core.exceptions import ObjectDoesNotExist


def IndexView(request):
    return render(request, 'index.html')


@login_required
def DashboardView(request):
    return render(request, 'dashboard.html')


def SignUpView(request):
    if request.method == "POST":
        form1 = RegistrationForm(request.POST)
        if form1.is_valid():
            form1.save()
            print('')
            Max = 9999999
            account_number = random.randint(0, Max)
            password1 = BaseUserManager().make_random_password
            c_id = Customer.objects.filter(card_no= form1.cleaned_data['card_no']).first()
            Account.objects.create(account_no=account_number, password=password1, limit=100000000, balance=50000,
                                   create_day=datetime.date.today(), end_day=datetime.date.today() + timedelta(days=3650), status=1,
                                   customer_id=c_id)
            print('x')
            return HttpResponse('hhahahaha')
    else:
        form1 = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form1})


def LoginView(request):
    if request.method == 'POST':
        username1 = request.POST['usr']
        password1 = request.POST['pas']
        if Account.objects.filter(account_no=username1, password=password1).exists():
            request.session['usr'] = username1
            request.session.set_expiry(10)
            return render(request, 'dashboard.html/')
        else:
            return HttpResponse("sai ten dang nhap hoac mat khau")
    else:
        return render(request, 'registration/login.html')


def WithdrawalView(request):
    if request.method == 'POST':
        data = request.POST.copy()
        amount = data['amount']
        print(data)
        try:
            amount = int(amount)
            return HttpResponse('Rút thành công %d VNĐ!' % amount)
            # account = Account.objects.filter('')
        except:
            return HttpResponse('Số tiền méo đúng rùi!')
            # if Account.objects.filter(balance__gte=)
    return render(request, 'withdrawal.html')

