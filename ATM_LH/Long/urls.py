from django.urls import path, include
from django.contrib.auth import views as auth_views
from Long.views import LoginAdmin, change_password_admin, logout_admin, FindProvince, \
                        FindBranch, AddProvince, home_view, open_new_card
app_name = 'Long'
urlpatterns = [
    path('login/', LoginAdmin.as_view(), name='login'),
    path('change/', change_password_admin, name='change'),
    path('logout/', logout_admin, name='logout'),
    # reset hoan thien
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_done'),
    # confirm password
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'
    ),
    # Yeu cau reset password
    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html'), name='password_reset'),
    # Reset hoan thanh
    path('reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_complete.html'), name='password_reset_complete'
    ),
    path('find/province/', FindProvince.as_view(), name='province_find'),
    path('add/province/', AddProvince.as_view(), name='add_province'),
    path('find/branch/view/', FindBranch.as_view(), name='view_branch'),
    path('open/card/', open_new_card, name='open_card'),
    path('home/', home_view, name='home')
]