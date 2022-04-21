from re import template
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('accounts/signin/', auth_views.LoginView.as_view(template_name='accounts/signin.html', redirect_authenticated_user=True), name='signin'),
    path('accounts/signin/', views.login_view, name="signin"),
    path('accounts/signup/', views.signup, name='signup'),
    path("accounts/signout/", auth_views.LogoutView.as_view(next_page='/accounts/accounts/signin'), name="signout"),
    path('resendOTP', views.resend_otp),
    path('accounts/profile/', views.profile, name="profile"),
    path('password-reset/', views.ResetPasswordView.as_view(), name='password_reset'),

    path('accounts/password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('accounts/password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),

    path('accounts/password-change/', views.ChangePasswordView.as_view(), name='changepassword'),

]
