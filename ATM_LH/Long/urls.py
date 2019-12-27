from django.urls import path
from Long.views import Home
from django.conf.urls import url
from Long.views import signup, add_inf, signup_customer

app_name = 'Long'
urlpatterns = [
    path('home/', Home, name='home'),
    path('signup/', signup_customer, name='signup'),
    path('add/', add_inf, name='addinf'),
]
