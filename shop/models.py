from enum import unique
from django.db import models
from django.contrib.auth.models import User
from gfx.models import Product
# Create your models here.

# class Cart(models.Model):
#     cart_id = models.AutoField(primary_key=True)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     created_on = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.cart_id) + 'by' + self.request.user.email

# class ProductInCart(models.Model):
#     class Meta:
#         unique_together = (('cart', 'Product'))
#     product_in_Cart_id = models.AutoField(primary_key=True)
#     cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)

# class Order(models.Model):
#     total_amount = models.FloatField()
#     order_id = models.CharField(unique=True, max_length=100, null=True, blank=True, default=None) 
#     datetime_of_payment = models.DateTimeField(auto_now_add=True)
#     # related to razorpay
#     razorpay_order_id = models.CharField(max_length=500, null=True, blank=True)
#     razorpay_payment_id = models.CharField(max_length=500, null=True, blank=True)
#     razorpay_signature = models.CharField(max_length=500, null=True, blank=True)
    

#     def save(self, *args, **kwargs):
#         if self.order_id is None and self.datetime_of_payment and self.id:
#             self.order_id = self.datetime_of_payment.strftime('PAY2ME%Y%m%dODR') + str(self.id)
#         return super().save(*args, **kwargs)

#     def __str__(self):
#         return self.user.email + " " + str(self.id)

# class ProductInOrder(models.Model):
#     class Meta:
#         unique_together = (('order', 'product'),)
#     order = models.ForeignKey(Order, on_delete = models.CASCADE)
#     product = models.ForeignKey(Product, on_delete = models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     price = models.FloatField()