from django.contrib import admin
from .models import Profile
# # Register your models here.

admin.site.site_header = "Nawab Editz"
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "about_me", "gender")