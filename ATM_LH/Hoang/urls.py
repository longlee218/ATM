from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login_url'),
    path('dashboard/', views.DashboardView, name='dashboard'),
    path('register/', views.RegisterView, name='register'),
    path('', views.IndexView, name='view'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
