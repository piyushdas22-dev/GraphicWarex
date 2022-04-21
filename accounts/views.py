import re
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages 
from django.views import View
from .forms import AccountRegister, AccountSignin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
import random
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import UserOTP, Profile
from django.conf import settings
from django.http import HttpResponse, Http404, JsonResponse
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import PasswordChangeForm
from .forms import *
from django.contrib.auth import update_session_auth_hash
from .helpers import send_forget_password_mail
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView

# Create your views here.




def signup(request):
	if request.method == 'POST':
		get_otp = request.POST.get('otp') #213243 #None

		if get_otp:
			get_usr = request.POST.get('usr')
			usr = User.objects.get(username=get_usr)
			if int(get_otp) == UserOTP.objects.filter(user = usr).last().otp:
				usr.is_active = True
				usr.save()
				messages.success(request, f'Account is Created For {usr.username}')
				return redirect('/accounts/accounts/signin')
			else:
				messages.warning(request, f'You Entered a Wrong OTP')
				return render(request, 'accounts/signup.html', {'otp': True, 'usr': usr})

		form = AccountRegister(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')

			usr = User.objects.get(username=username)
			usr.is_active = False
			usr.save()
			usr_otp = random.randint(100000, 999999)
			UserOTP.objects.create(user = usr, otp = usr_otp)

			mess = f"Hello {usr.username},\nYour OTP is {usr_otp}\n Please Verify to SignIn Thanks!"

			send_mail(
				"Welcome to Nawabeditz - Please Verify Your Email",
				mess,
				settings.EMAIL_HOST_USER,
				[usr.email],
				fail_silently = False
				)

			return render(request, 'accounts/signup.html', {'otp': True, 'usr': usr})

		
	else:
		form = AccountRegister()

	return render(request, 'accounts/signup.html', {'form':form})
        
def resend_otp(request):
	if request.method == "GET":
		get_usr = request.GET['usr']
		if User.objects.filter(username = get_usr).exists() and not User.objects.get(username = get_usr).is_active:
			usr = User.objects.get(username=get_usr)
			usr_otp = random.randint(100000, 999999)
			UserOTP.objects.create(user = usr, otp = usr_otp)
			mess = f"Hello {usr.username},\nYour OTP is {usr_otp}\nThanks!"

			send_mail(
				"Welcome to NawabEditz - Please Verify Your Email",
				mess,
				settings.EMAIL_HOST_USER,
				[usr.email],
				fail_silently = False
				)
			return HttpResponse("Resend")

	return HttpResponse("Can't Send ")
def login_view(request):
	if request.user.is_authenticated:
		return redirect('profile')
	if request.method == 'POST':
		get_otp = request.POST.get('otp') #213243 #None

		if get_otp:
			get_usr = request.POST.get('usr')
			usr = User.objects.get(username=get_usr)
			if int(get_otp) == UserOTP.objects.filter(user = usr).last().otp:
				usr.is_active = True
				usr.save()
				login(request, usr)
				return redirect('/')
			else:
				messages.warning(request, f'You Entered a Wrong OTP')
				return render(request, 'accounts/signin.html', {'otp': True, 'usr': usr})


		usrname = request.POST['username']
		passwd = request.POST['password']

		user = authenticate(request, username = usrname, password = passwd) #None
		if user is not None:
			login(request, user)
			return redirect('profile')
		elif not User.objects.filter(username = usrname).exists():
			messages.warning(request, f'Please enter a correct username and password. Note that both fields may be case-sensitive.')
			return redirect('signin')
		elif not User.objects.get(username=usrname).is_active:
			usr = User.objects.get(username=usrname)
			usr_otp = random.randint(100000, 999999)
			UserOTP.objects.create(user = usr, otp = usr_otp)
			mess = f"Hello {usr.username},\nYour OTP is {usr_otp}\nThanks!"

			send_mail(
				"Welcome to Nawab Editz - Verify Your Email",
				mess,
				settings.EMAIL_HOST_USER,
				[usr.email],
				fail_silently = False
				)
			return render(request, 'accounts/signin.html', {'otp': True, 'usr': usr})
		else:
			messages.warning(request, f'Please enter a correct username and password. Note that both fields may be case-sensitive.')
			return redirect('/accounts/accounts/signin')

	form = AccountSignin()
	return render(request, 'accounts/signin.html', {'form': form})

@login_required(login_url="signin")
def profile(request):
	if request.method == "POST":
		form = UsernameForm(request.POST, instance=request.user)
		user_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
		user_form.save()
		form.save()
		messages.success(request, "Your profile is updated successfully")
	else:
		form = UsernameForm(instance=request.user)
		user_form = ProfileForm(instance=request.user.profile)
	return render(request, 'accounts/profile.html', {'form': form, 'user_form': user_form})


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject'
    success_message = "Successfully reseted your password, please login " 
    success_url = reverse_lazy('password_reset')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('changepassword')