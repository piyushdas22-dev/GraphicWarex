from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from .choices import *
import datetime
# Create your models here.

class UserDesignCat(models.Model):
    name = models.CharField(max_length=99)

    def __str__(self) -> str:
        return self.name
        
class WarexDesignCat(models.Model):
    name = models.CharField(max_length=99)

    def __str__(self) -> str:
        return self.name

class FreePackCat(models.Model):
    name = models.CharField(max_length=99)

    def __str__(self) -> str:
        return self.name

class PaidPackCat(models.Model):
    name = models.CharField(max_length=99)

    def __str__(self) -> str:
        return self.name

class UserPackCat(models.Model):
    name = models.CharField(max_length=99)

    def __str__(self) -> str:
        return self.name

class WarexDesign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    details = models.TextField(default="Write description here....")
    image = models.ImageField(upload_to="WarexDesign_Images/")
    category = models.ForeignKey(WarexDesignCat, on_delete=models.CASCADE)
    download_link = models.CharField(max_length=999, blank=True)
    is_deleted = models.BooleanField(default=False)
    sp = models.IntegerField(default=0)
    dp = models.IntegerField(default=0)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        order_with_respect_to = 'title'

class FreePack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    details = models.TextField(default="Write description here....")
    image = models.ImageField(upload_to="FreePack_Images/")
    category = models.ForeignKey(FreePackCat, on_delete=models.CASCADE)
    download_link = models.CharField(max_length=999, blank=True)
    is_deleted = models.BooleanField(default=False)
    sp = models.IntegerField(default=0)
    dp = models.IntegerField(default=0)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        order_with_respect_to = 'title'


class PaidPack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    details = models.TextField(default="Write description here....")
    image = models.ImageField(upload_to="Paid_Images/")
    category = models.ForeignKey(PaidPackCat, on_delete=models.CASCADE)
    download_link = models.CharField(max_length=999, blank=True)
    is_deleted = models.BooleanField(default=False)
    sp = models.IntegerField(default=0)
    dp = models.IntegerField(default=0)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        order_with_respect_to = 'title'
    

class UserDesign(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    details = models.TextField(default="Write description here....")
    image = models.ImageField(upload_to="UserDesign_Images/")
    category = models.ForeignKey(UserDesignCat, on_delete=models.CASCADE)
    download_link = models.CharField(max_length=999, blank=True)
    is_deleted = models.BooleanField(default=False)
    sp = models.IntegerField(default=0)
    dp = models.IntegerField(default=0)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        order_with_respect_to = 'title'

class UserPack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    details = models.TextField(default="Write description here....")
    image = models.ImageField(upload_to="UserPack_Images/")
    category = models.ForeignKey(UserPackCat, on_delete=models.CASCADE)
    download_link = models.CharField(max_length=999, blank=True)
    is_deleted = models.BooleanField(default=False)
    sp = models.IntegerField(default=0)
    dp = models.IntegerField(default=0)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    views = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        order_with_respect_to = 'title'

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    details = models.TextField(default="...")
    image = models.ImageField(upload_to="Product_Images/")
    category = models.CharField(choices=CHOICES, default='--', max_length=90)
    download_link = models.CharField(max_length=999, blank=True)
    status = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    sp = models.IntegerField(default=0)
    dp = models.IntegerField(default=0)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    views = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    
    class Meta:
        order_with_respect_to = 'title'

# WishList
class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Wishlist'


class PartnersName(models.Model):
    name = models.CharField(max_length=99)

    class Meta:
        verbose_name_plural = 'Partners'

    def __str__(self) -> str:
        return self.name

class PartnersPack(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    partner = models.ForeignKey(PartnersName, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    details = models.TextField(default="...")
    image = models.ImageField(upload_to="PartnerPack_Images/")
    download_link = models.CharField(max_length=999, blank=True)
    is_deleted = models.BooleanField(default=False)
    sp = models.IntegerField(default=0)
    dp = models.IntegerField(default=0)
    date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title + 'by' + self.partner.name
    
    class Meta:
        order_with_respect_to = 'title'