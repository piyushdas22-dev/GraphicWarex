from django.db import models
from django.contrib.auth.models import User
from .choices import *
import datetime
# Create your models here.

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    details = models.TextField(default="...")
    image = models.ImageField(upload_to="GFXPack_Images/")
    category = models.CharField(choices=CHOICES, default='--', max_length=90)
    order_link = models.CharField(max_length=999, blank=True)
    download_link = models.CharField(max_length=999, blank=True)
    buy_link = models.CharField(max_length=999, blank=True)
    status = models.BooleanField(default=False)
    trending = models.BooleanField(default=False)
    sp = models.IntegerField(default=0)
    dp = models.IntegerField(default=0)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    
    class Meta:
        order_with_respect_to = 'title'