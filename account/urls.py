from re import template
from django.shortcuts import redirect
from django.urls import path, reverse_lazy
from . import views
from django.shortcuts import redirect
from django.contrib.auth.views import (LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView,
PasswordResetView, PasswordResetDoneView,PasswordResetConfirmView, PasswordResetCompleteView)

import account


app_name='account'
urlpatterns=[
    #path('', views.user_login, name='login')
    path('', views.home, name='home'),

    path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),

    #password change urls
    path('password-change/', PasswordChangeView.as_view(template_name='account/password_change_form.html', success_url = reverse_lazy('account:password_change_done')), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'), name='password_change_done'),

    #password reset urls
    path('password-reset/', PasswordResetView.as_view(template_name='account/password_reset_form.html', success_url = reverse_lazy('account:password_reset_done'), email_template_name = 'account/password_reset_email.html'), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='account/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html', success_url=reverse_lazy('account:password_reset_complete')), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'), name='password_reset_complete')

]