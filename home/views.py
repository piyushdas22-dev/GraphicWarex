from unicodedata import category
from django import views
from django.shortcuts import render
from accounts.models import Profile
from .models import Category, Slider
from gfx.models import Product
from .forms import ContactForm
from django.shortcuts import redirect, render
from django.contrib import messages 
from django.core.mail import send_mail
from .forms import *

# Create your views here.


def home(request):
    trends = Product.objects.filter(views__gte = 100,trending = True).order_by("-views")
    sliders = Slider.objects.all()
    return render(request, 'home/home.html', {'sliders': sliders, 'trends': trends})


def about(request):
    return render(request, 'home/about.html')


def communityguidelines(request):
    return render(request, 'home/communityguidelines.html')


def privacypolicy(request):
    return render(request, 'home/privacypolicy.html')

# Create your views here.

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Nawab Editz Contact"
            body = {'email': form.cleaned_data['email'], 'content': form.cleaned_data['content']}
            message = '\n'.join(body.values())
            send_mail(subject,message, 'ptsprogrammer@gmail.com', ['daspiyush773@gmail.com'])
        

    form = ContactForm()
    return render(request, "contact/contact.html", {'form':form})

def nawabdesigns(request):
    category = Category.objects.all()
    return render(request, "category/category.html", {'category': category})