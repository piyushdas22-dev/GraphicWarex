from django.urls import path
from . import views
urlpatterns = [
    path('paidpacks/', views.PaidPacks, name='paidpacks'),
    path('paidpacks/post/', views.AddPaidPacks, name="paidpackspost"),

    path('userpacks/', views.UserPacks, name='userpacks'),
    path('userpacks/post/', views.AddUserPacks, name="userpackspost"),

    path('freepacks/', views.FreePacks, name='freepacks'),
    path('freepacks/post/', views.AddFreePacks, name="freepackspost"),


    path('warexdesigns/', views.WarexDesigns, name='WarexDesign'),
    path('warexdesigns/post/', views.AddWarexDesigns, name="warexpost"),

    path('userdesigns/', views.UserDesigns, name='userdesigns'),
    path('userdesign/post/', views.AddUserDesigns, name="userdesignspost"),

    path("delete/<int:pk>/", views.delete, name="delete-post"),
    path('your-posts/', views.uploaded_posts, name="userposts"),
    path('editpost/<id>', views.editpost, name="editpost"),

    path('ytpacks/', views.partnerspack, name="partnerpacks"),
    path("deletepost/<int:pk>/", views.delete, name="delete-partner-post"),
    path('editposts/<id>', views.editpost, name="editpartnerpost"),
]
