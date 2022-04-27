from django.contrib import admin
from .models import  Product, Wishlist, PartnersName, PartnersPack, WarexDesign, WarexDesignCat, UserDesignCat, UserDesign, FreePackCat, FreePack, PaidPack, PaidPackCat, UserPack, UserPackCat
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "category", "views", "status", "is_deleted")
    list_editable = ("status", "is_deleted")

admin.site.register(Wishlist)
admin.site.register(PartnersName)
admin.site.register(WarexDesignCat)
admin.site.register(UserDesignCat)
admin.site.register(FreePackCat)
admin.site.register(PaidPackCat)
admin.site.register(UserPackCat)

@admin.register(PartnersPack)
class PartnersPackAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "views", "is_deleted", "partner")
    list_editable = ("is_deleted",)

@admin.register(WarexDesign)
class WarexDesignAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "views", "is_deleted", "is_deleted")
    list_editable = ("is_deleted",)

@admin.register(UserDesign)
class UserDesignAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "views", "is_deleted", "is_deleted")
    list_editable = ("is_deleted",)

@admin.register(FreePack)
class FreePackAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "views", "is_deleted", "is_deleted")
    list_editable = ("is_deleted",)

@admin.register(PaidPack)
class PaidPackAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "views", "is_deleted", "is_deleted")
    list_editable = ("is_deleted",)

@admin.register(UserPack)
class UserPackAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "views", "is_deleted", "is_deleted")
    list_editable = ("is_deleted",)