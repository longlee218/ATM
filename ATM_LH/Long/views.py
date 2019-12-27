from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from .forms import SignUp
# Create your views here.


def Home(request):
    return render(request, 'Long/index.html', {})


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


def add_inf(request):
    infor = SignUp()
    return render(request, 'Long/signup.html', {'info': infor})


def signup_customer(request):
    if request.method == 'POST':
        post_forms = SignUp(request.POST)
        if post_forms.is_valid():
            post_forms.save()
            return HttpResponse('Luu thanh cong')
        else:
            return HttpResponse('Khong luu thanh cong, du lieu ko validate')
    else:
        return HttpResponse('Khong phai request post')
