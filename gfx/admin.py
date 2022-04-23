from django.contrib import admin
from .models import  Product,CartOrder, CartOrderItems, Wishlist, ProductReview
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "views", "status", "is_deleted")
    list_editable = ("status", "is_deleted")

admin.site.register(CartOrderItems)
admin.site.register(CartOrder)
admin.site.register(Wishlist)
admin.site.register(ProductReview)
# admin.site.register(YTPACKS)