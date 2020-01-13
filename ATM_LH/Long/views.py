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
# Create your views here.


def Home(request):
    return render(request, 'Long/index.html', {})

#dang ky nguoi dung
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('Username')
            raw_password = form.cleaned_data.get('PassWord')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'Long/login.html', {'form': form})


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
