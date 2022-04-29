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
    path("delete2/<int:pk>/", views.delete2, name="delete-post2"),
    path("delete3/<int:pk>/", views.delete3, name="delete-post3"),
    path("delete4/<int:pk>/", views.delete4, name="delete-post4"),
    path("delete5/<int:pk>/", views.delete5, name="delete-post5"),
    path("delete5/<int:pk>/", views.delete6, name="delete-post6"),

    path('your-posts/', views.uploads, name="userposts"),

    path('editpost/<id>', views.editpost, name="editpost"),
    path('editpost2/<id>', views.editpost2, name="editpost2"),
    path('editpost3/<id>', views.editpost3, name="editpost3"),
    path('editpost4/<id>', views.editpost4, name="editpost4"),
    path('editpost5/<id>', views.editpost5, name="editpost5"),
    path('editpost6/<id>', views.editpost6, name="editpost6"),

    path('ytpacks/', views.partnerspack, name="partnerpacks"),
    path('post/', views.AddPartnerPack, name="partnerpackspost"),
    path("deletepost/<int:pk>/", views.delete, name="delete-partner-post"),
    path('editposts/<id>', views.editpost, name="editpartnerpost"),
]
