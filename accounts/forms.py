from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
from django.contrib.auth.models import User
from django.utils.translation import gettext, gettext_lazy as _
from django.core.exceptions import ValidationError
from .models import Profile

class AccountRegister(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Confirm Password (again)', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2' ]
        labels = {'email': 'Email'}
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'})}

class AccountSignin(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(attrs={'class':'form-control'}))

class ProfileForm(forms.ModelForm):
    about_me = forms.CharField(label='About Me', widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    profile_pic = forms.FileField(label='Profile Photo', widget=forms.FileInput(attrs={'class':'form-control'}), required=False)
    gender = forms.ChoiceField(label='Gender', choices= (('--', '------'),('M', 'MALE'),('F', 'FEMALE'), ('P', 'OTHER')) ,widget=forms.Select(attrs={'class':'form-control'}), required=False)


    class Meta:
        model = Profile
        fields = ['about_me', 'profile_pic', 'gender']

class UsernameForm(forms.ModelForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'email']