from unicodedata import category
from django.db import models
from django.contrib.auth.models import User
from .choices import *
import datetime
# Create your models here.

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

# class YTPACKS(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
#     title = models.CharField(max_length=150)
#     details = models.TextField(default="...")
#     image = models.ImageField(upload_to="GFXPack_Images/")
#     category = models.CharField(choices=YT_PACKS_CHOICES, default='--', max_length=90)
#     download_link = models.CharField(max_length=999, blank=True)
#     date_uploaded = models.DateTimeField(auto_now_add=True, null=True)
#     is_deleted = models.BooleanField(default=False)
#     views = models.IntegerField(default=0)

#     def __str__(self):
#         return self.title + 'By' + self.user
    
#     class Meta:
#         order_with_respect_to = 'title'

class CartOrder(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    total_amt=models.FloatField()
    paid_status=models.BooleanField(default=False)
    order_dt=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural='Orders'

# OrderItems
class CartOrderItems(models.Model):
    order=models.ForeignKey(CartOrder,on_delete=models.CASCADE)
    invoice_no=models.CharField(max_length=150)
    item=models.CharField(max_length=150)
    image=models.CharField(max_length=200)
    price=models.FloatField()
    total=models.FloatField()

    class Meta:
        verbose_name_plural='Order Items'

# Product Review
RATING=(
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),
)
class ProductReview(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    review_text=models.TextField()
    review_rating=models.CharField(choices=RATING,max_length=150)

    class Meta:
        verbose_name_plural='Reviews'

    def get_review_rating(self):
        return self.review_rating

# WishList
class Wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural='Wishlist'
    