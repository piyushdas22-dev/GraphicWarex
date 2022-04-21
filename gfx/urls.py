from django.urls import path
from . import views
urlpatterns = [
    path('paidpacks/thumbnails', views.paidthumbnailpack, name='paidthumbnailpacks'),
    path('paidpacks/banners', views.paidbannerpack, name='paidbannerpacks'),
    path('paidpacks/intros', views.paidintropack, name='paidintropacks'),
    path('paidpacks/outros', views.paidoutropack, name='paidoutropacks'),
    path('paidpacks/posters', views.paidposterpack, name='paidposterpacks'),
    path('paidpacks/renders', views.paidrenderpack, name='paidrenderpacks'),
    path('paidpacks/gfxmaterials', views.paidgfxmaterialspack, name='paidgfxmaterialspacks'),

    path('userpacks/thumbnails', views.userpacksthumbnail, name='userpacksthumbnail'),
    path('userpacks/banners', views.userpacksbanner, name='userpacksbanner'),
    path('userpacks/intros', views.userpacksintro, name='userpacksintro'),
    path('userpacks/outros', views.userpacksoutro, name='userpacksoutro'),
    path('userpacks/posters', views.userpacksposter, name='userpacksposter'),
    path('userpacks/renders', views.userpacksrender, name='userpacksrender'),
    path('userpacks/gfxmaterials', views.userpacksgfxmaterials, name='userpacksgfxmaterials'),
    path('userpacks/post/', views.AddUserPacks, name="userpackspost"),

    path('freepacks/thumbnails/', views.freepacksthumbnail, name='freepacksthumbnail'),
    path('freepacks/banners/', views.freepacksbanner, name='freepacksbanner'),
    path('freepacks/intros/', views.freepacksintro, name='freepacksintro'),
    path('freepacks/outros/', views.freepacksoutro, name='freepacksoutro'),
    path('freepacks/posters/', views.freepacksposter, name='freepacksposter'),
    path('freepacks/renders/', views.freepacksrender, name='freepacksrender'),
    path('freepackspacks/post/', views.AddFreePacks, name="freepackspost"),


    path('nawabdesigns/thumbnails/', views.thumbnails, name='thumbnails'),
    path('nawabdesigns/banner/', views.banners, name='banners'),
    path('nawabdesigns/intro/', views.intros, name='intros'),
    path('nawabdesigns/outro/', views.outros, name='outros'),
    path('nawabdesigns/posters/', views.posters, name='posters'),
    path('nawabdesigns/others/', views.others, name='others'),
    path('nawabdesigns/post/', views.AddNawabDesigns, name="nawabdesignspost"),

    path('userdesigns/thumbnails/', views.userdesignsthumbnail, name='userdesignsthumbnails'),
    path('userdesigns/banner/', views.userdesignsbanner, name='userdesignsbanners'),
    path('userdesigns/intro/', views.userdesignsintro, name='userdesignsintros'),
    path('userdesigns/outro/', views.userdesignsoutro, name='userdesignsoutros'),
    path('userdesigns/posters/', views.userdesignsposters, name='userdesignsposters'),
    path('userdesigns/others/', views.userdesignsothers, name='userdesignsothers'),
    path('userdesign/post/', views.AddUserDesigns, name="userdesignspost"),

    path('paidpacks/thumbnails/thumbnail_details/<int:pk>', views.PaidPacksThumbnailDetails.as_view(), name="paidpacksthumbnaildetails"),
    path('paidpacks/banner/banner_details/<int:pk>', views.PaidPacksBannerDetails.as_view(), name="paidpacksbannerdetails"),
    path('paidpacks/intro/intro_details/<int:pk>', views.PaidPacksIntroDetails.as_view(), name="paidpacksintrodetails"),
    path('paidpacks/outro/outro_details/<int:pk>', views.PaidPacksOutroDetails.as_view(), name="paidpacksoutrodetails"),
    path('paidpacks/poster/poster_details/<int:pk>', views.PaidPacksPosterDetails.as_view(), name="paidpacksposterdetails"),
    path('paidpacks/render/render_details/<int:pk>', views.PaidPacksRenderDetails.as_view(), name="paidpacksrenderdetails"),
    path('paidpacks/gfxmaterials/gfxmaterials_details/<int:pk>', views.PaidPacksGFXMaterialDetails.as_view(), name="paidpacksgfxmaterialsdetails"),
    path('paidpacks/post/', views.AddPaidPacks, name="paidpackspost"),

    path("delete/<id>/", views.delete, name="delete-post"),
]
