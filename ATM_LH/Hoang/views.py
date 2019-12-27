from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm


def IndexView(request):
    return render(request, 'index.html')


@login_required
def DashboardView(request):
    return render(request, 'dashboard.html')


def RegisterView(request):
    form = RegistrationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return HttpResponse("Dang ki thanh cong")
        else:
            return HttpResponse("invalid")
    return render(request, 'registration/register.html', {'form': form})