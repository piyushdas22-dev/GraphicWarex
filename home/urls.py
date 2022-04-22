from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('trending/', views.trending, name="trending"),
    path('recent_post/', views.recent, name="recent"),
    path('about/', views.about, name="about"),
    path('communityguidelines', views.communityguidelines, name="communityguidelines"),
    path('privacypolicy', views.privacypolicy, name="privacypolicy"),
    path('nawabdesigns', views.nawabdesigns, name="nawabdesigns")
]
