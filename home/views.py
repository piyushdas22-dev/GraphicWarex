from unicodedata import category
from django import views
from django.shortcuts import render
from accounts.models import Profile
from .models import Category, HomeNumber, Slider, TrendingSlider
from gfx.models import Product, WarexDesign
from .forms import ContactForm
from django.shortcuts import redirect, render
from django.contrib import messages 
from django.core.mail import send_mail
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    trends = Product.objects.filter(views__gte = 100,is_deleted=False).order_by("-views")
    recent = Product.objects.filter(is_deleted=False).order_by("-date_uploaded")
    sliders = Slider.objects.all()
    Trendingslider = TrendingSlider.objects.all()
    number = HomeNumber.objects.all()
    return render(request, 'home/home.html', {'sliders': sliders, 'Trendingslider': Trendingslider, 'trends': trends, 'recent': recent, 'number': number})

def recent(request):
    recent = Product.objects.filter(is_deleted=False).order_by("-date_uploaded")
    return render(request, 'home/recent.html', {'recent': recent})

def trending(request):
    trends = Product.objects.filter(views__gte = 100,is_deleted=False).order_by("-views") 
    Trendingslider = TrendingSlider.objects.all()
    return render(request, 'home/trending.html', {'Trendingslider': Trendingslider, 'trends': trends})


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