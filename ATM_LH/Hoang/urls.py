from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.LoginView, name='login_url'),
    path('dashboard/', views.DashboardView, name='dashboard'),
    path('register/', views.SignUpView, name='register'),
    path('withdrawal/', views.WithdrawalView, name='withdrawal'),
    # path('dashboard/withdrawal/', )
]