from django.contrib import admin
from .models import HomeNumber, Slider, TrendingSlider

# Register your models here.

admin.site.register(Slider)
admin.site.register(TrendingSlider)
admin.site.register(HomeNumber)
