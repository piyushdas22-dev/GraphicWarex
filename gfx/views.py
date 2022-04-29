from itertools import product
from math import prod
from re import template
from unicodedata import category, name
from django import views
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views import View
from .models import *
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import AddPartnersPackForm, AddWarexDesignForm, AddUserProductForm, AddFreePackForm, AddPaidPackForm, AddUserPackForm


def thumbnails(request):
    thumbnails = Product.objects.filter(category='NT', is_deleted=False)
    return render(request, 'gfx/nawabdesigns/nawabdesignsthumbnails.html', {'thumbnails': thumbnails})


def banners(request):
    banners = Product.objects.filter(category='NB',is_deleted=False)
    return render(request, 'gfx/nawabdesigns/nawabdesignsbanners.html', {'banners': banners})


def intros(request):
    intros = Product.objects.filter(category='NI',is_deleted=False)
    return render(request, 'gfx/nawabdesigns/nawabdesignsintros.html', {'intros': intros})


def outros(request):
    outros = Product.objects.filter(category='NO',is_deleted=False)
    return render(request, 'gfx/nawabdesigns/nawabdesignsoutros.html', {'outros': outros})


def posters(request):
    posters = Product.objects.filter(category='NP',is_deleted=False)
    return render(request, 'gfx/nawabdesigns/nawabdesignsposters.html', {'posters': posters})


def others(request):
    others = Product.objects.filter(category='NOth',is_deleted=False)
    return render(request, 'gfx/nawabdesigns/nawabdesignsothers.html', {'others': others})


def paidthumbnailpack(request):
    thumbnails = Product.objects.filter(category='PPT',is_deleted=False)
    return render(request, 'gfx/paidpacks/thumbnailpack.html', {'thumbnails': thumbnails})


def paidbannerpack(request):
    banners = Product.objects.filter(category='PPB',is_deleted=False)
    return render(request, 'gfx/paidpacks/bannerpack.html', {'banners': banners})


def paidintropack(request):
    intros = Product.objects.filter(category='PPI',is_deleted=False)
    return render(request, 'gfx/paidpacks/intropack.html', {'intros': intros})


def paidoutropack(request):
    outros = Product.objects.filter(category='PPO',is_deleted=False)
    return render(request, 'gfx/paidpacks/outropack.html', {'outros': outros})


def paidrenderpack(request):
    renders = Product.objects.filter(category='PPR',is_deleted=False)
    return render(request, 'gfx/paidpacks/renderpack.html', {'renders': renders})


def paidgfxmaterialspack(request):
    gfxmaterials = Product.objects.filter(category='PPG',is_deleted=False)
    return render(request, 'gfx/paidpacks/gfxmaterialspack.html', {'gfxmaterials': gfxmaterials})


def paidposterpack(request):
    posters = Product.objects.filter(category='PPP',is_deleted=False)
    return render(request, 'gfx/paidpacks/posterpack.html', {'posters': posters})


def freepacksthumbnail(request):
    freepacksthumb = Product.objects.filter(category='FPT',is_deleted=False)
    return render(request, 'gfx/freepacks/thumbnail.html', {'freepacksthumb': freepacksthumb})


def freepacksbanner(request):
    freepacksban = Product.objects.filter(category='FPB',is_deleted=False)
    return render(request, 'gfx/freepacks/banner.html', {'freepacksban': freepacksban})


def freepacksintro(request):
    freepacksintro = Product.objects.filter(category='FPI',is_deleted=False)
    return render(request, 'gfx/freepacks/intro.html', {'freepacksintro': freepacksintro})


def freepacksoutro(request):
    freepacksoutro = Product.objects.filter(category='FPO',is_deleted=False)
    return render(request, 'gfx/freepacks/outro.html', {'freepacksoutro': freepacksoutro})


def freepacksrender(request):
    freepacksrender = Product.objects.filter(category='FPR',is_deleted=False)
    return render(request, 'gfx/freepacks/renders.html', {'freepacksrender': freepacksrender})


def freepacksposter(request):
    freepacksposter = Product.objects.filter(category='FPP',is_deleted=False)
    return render(request, 'gfx/freepacks/poster.html', {'freepacksposter': freepacksposter})


def userpacksthumbnail(request):
    userpacksthumbnail = Product.objects.filter(category='UGT', status=True,is_deleted=False)
    # userpacksthumbnail = UserGFXPack.objects.filter(status=True)
    return render(request, 'gfx/userpacks/thumbnail.html', {'userpacksthumbnail': userpacksthumbnail})


def userpacksbanner(request):
    userpacksbanner = Product.objects.filter(category='UGB', status=True,is_deleted=False)
    return render(request, 'gfx/userpacks/banner.html', {'userpacksbanner': userpacksbanner})


def userpacksintro(request):
    userpacksintro = Product.objects.filter(category='UGI', status=True,is_deleted=False)
    return render(request, 'gfx/userpacks/intro.html', {'userpacksintro': userpacksintro})


def userpacksoutro(request):
    userpacksoutro = Product.objects.filter(category='UGO', status=True,is_deleted=False)
    return render(request, 'gfx/userpacks/outro.html', {'userpacksoutro': userpacksoutro})


def userpacksposter(request):
    userpacksposter = Product.objects.filter(category='UGP', status=True,is_deleted=False)
    return render(request, 'gfx/userpacks/poster.html', {'userpacksposter': userpacksposter})


def userpacksrender(request):
    userpacksrender = Product.objects.filter(category='UGR', status=True,is_deleted=False)
    return render(request, 'gfx/userpacks/render.html', {'userpacksrender': userpacksrender})


def userpacksgfxmaterials(request):
    userpacksgfxmaterials = Product.objects.filter(
        category='UGG', status=True,is_deleted=False)
    return render(request, 'gfx/userpacks/gfxmaterials.html', {'userpacksgfxmaterials': userpacksgfxmaterials})


def userdesignsthumbnail(request):
    userdesignsthumbnails = Product.objects.filter(
        category='UDT', status=True,is_deleted=False)
    return render(request, 'gfx/userdesigns/userdesignsthumbnail.html', {'userdesignsthumbnails': userdesignsthumbnails})


def userdesignsbanner(request):
    userdesignsbanners = Product.objects.filter(category='UDB', status=True,is_deleted=False)
    return render(request, 'gfx/userdesigns/userdesignsbanner.html', {'userdesignsbanners': userdesignsbanners})


def userdesignsintro(request):
    userdesignsintros = Product.objects.filter(category='UDI', status=True,is_deleted=False)
    return render(request, 'gfx/userdesigns/userdesignsintro.html', {'userdesignsintros': userdesignsintros})


def userdesignsoutro(request):
    userdesignsoutros = Product.objects.filter(category='UDO', status=True,is_deleted=False)
    return render(request, 'gfx/userdesigns/userdesignsoutro.html', {'userdesignsoutros': userdesignsoutros})


def userdesignsposters(request):
    userdesignsposters = Product.objects.filter(category='UDP', status=True,is_deleted=False)
    return render(request, 'gfx/userdesigns/userdesignsposters.html', {'userdesignsposters': userdesignsposters})


def userdesignsothers(request):
    userdesignsothers = Product.objects.filter(category='UDOth', status=True,is_deleted=False)
    return render(request, 'gfx/userdesigns/userdesignsothers.html', {'userdesignsothers': userdesignsothers})

# def nawabdesigns_thumbnail_details(request):
#     return render(request, "gfx/nawabdesigns/nawabdesigns_details/thumbnaildet.html")


class PaidPacksThumbnailDetails(View):
    def get(self, request, pk):
        thumbnaildet = Product.objects.get(pk=pk)
        return render(request, "gfx/paidpacks/paidpacks_details/thumbnaildet.html", {'thumbnaildet': thumbnaildet})


class PaidPacksBannerDetails(View):
    def get(self, request, pk):
        bannerdet = Product.objects.get(pk=pk)
        return render(request, "gfx/paidpacks/paidpacks_details/bannerdet.html", {'bannerdet': bannerdet})


class PaidPacksIntroDetails(View):
    def get(self, request, pk):
        introdet = Product.objects.get(pk=pk)
        return render(request, "gfx/paidpacks/paidpacks_details/introdet.html", {'introdet': introdet})


class PaidPacksOutroDetails(View):
    def get(self, request, pk):
        outrodet = Product.objects.get(pk=pk)
        return render(request, "gfx/paidpacks/paidpacks_details/outrodet.html", {'outrodet': outrodet})


class PaidPacksPosterDetails(View):
    def get(self, request, pk):
        posterdet = Product.objects.get(pk=pk)
        return render(request, "gfx/paidpacks/paidpacks_details/posterdet.html", {'posterdet': posterdet})


class PaidPacksRenderDetails(View):
    def get(self, request, pk):
        renderdet = Product.objects.get(pk=pk)
        return render(request, "gfx/paidpacks/paidpacks_details/renderdet.html", {'renderdet': renderdet})


class PaidPacksGFXMaterialDetails(View):
    def get(self, request, pk):
        gfxmaterialsdet = Product.objects.get(pk=pk)
        return render(request, "gfx/paidpacks/paidpacks_details/gfxmaterialsdet.html", {'gfxmaterialsdet': gfxmaterialsdet})




def delete(request, pk):
    """Function deletes user's post."""
    product = WarexDesign.objects.get(id=pk)
    if request.user.is_authenticated and request.user.is_superuser or request.user.is_staff:
        product.is_deleted = True
        product.save()
        messages.success(request, f'Successfully Deleted the Post')
    else:
        messages.warning(
            request, "You can't delete this upload, looks like this upload does'nt belongs to you.")
    return redirect('home')


def delete2(request, pk):
    """Function deletes user's post."""
    product = UserDesign.objects.get(id=pk)
    if request.user.is_authenticated and request.user == product.user or request.user.is_superuser or request.user.is_staff:
        product.is_deleted = True
        product.save()
        messages.success(request, f'Successfully Deleted the Post')
    else:
        messages.warning(
            request, "You can't delete this upload, looks like this upload does'nt belongs to you.")
    return redirect('home')

def delete3(request, pk):
    """Function deletes user's post."""
    product = FreePack.objects.get(id=pk)
    if request.user.is_authenticated and request.user.is_superuser or request.user.is_staff:
        product.is_deleted = True
        product.save()
        messages.success(request, f'Successfully Deleted the Post')
    else:
        messages.warning(
            request, "You can't delete this upload, looks like this upload does'nt belongs to you.")
    return redirect('home')


def delete4(request, pk):
    """Function deletes user's post."""
    product = PaidPack.objects.get(id=pk)
    if request.user.is_authenticated and request.user.is_superuser or request.user.is_staff:
        product.is_deleted = True
        product.save()
        messages.success(request, f'Successfully Deleted the Post')
    else:
        messages.warning(
            request, "You can't delete this upload, looks like this upload does'nt belongs to you.")
    return redirect('home')


def delete5(request, pk):
    """Function deletes user's post."""
    product = UserPack.objects.get(id=pk)
    if request.user.is_authenticated and request.user == product.user or request.user.is_superuser or request.user.is_staff:
        product.is_deleted = True
        product.save()
        messages.success(request, f'Successfully Deleted the Post')
    else:
        messages.warning(
            request, "You can't delete this upload, looks like this upload does'nt belongs to you.")
    return redirect('home')

def delete6(request, pk):
    """Function deletes user's post."""
    product = PartnersPack.objects.get(id=pk)
    if request.user.is_authenticated:
        product.is_deleted = True
        product.save()
        messages.success(request, f'Successfully Deleted the Post')
    else:
        messages.warning(
            request, "You can't delete this upload, looks like this upload does'nt belongs to you.")
    return redirect('home')
    
def AddUserPacks(request):
    if request.method == "POST":
        userform = AddUserPackForm(request.POST, request.FILES)
        if userform.is_valid():
            userpacks = userform.save(commit=False)
            userpacks.user = request.user
            userpacks.save()
            messages.success(request, f'Successfully Uploaded the post')
            return redirect('home')
        else:
            messages.info(request,"Something is wrong, Try Again")
    else:
        userform = AddUserPackForm()
    return render(request, "gfx/post/post.html", {'form': userform})


def AddPaidPacks(request):
    if request.method == "POST":
        addpacksform = AddPaidPackForm(request.POST, request.FILES)
        if addpacksform.is_valid() and request.user.is_superuser or request.user.is_staff:
            userpacks = addpacksform.save(commit=False)
            userpacks.user = request.user
            userpacks.save()
            messages.success(request, f'Successfully Uploaded the post')
            return redirect('home')
        else:
            messages.info("Something is wrong, Try Again")
    else:
        addpacksform = AddPaidPackForm()
    return render(request, "gfx/post/post.html", {'form': addpacksform})

def UserPacks(request):
    userp = FreePackCat.objects.all()
    UserpID = request.GET.get('userpacks')
    if UserpID:
        products = UserPack.objects.filter(category=UserpID).order_by('-date_uploaded')
        return render(request, 'gfx/userpacks/userpacks.html', {'userp': userp, 'products': products})
    else:
        products = UserPack.objects.all().order_by('-views')
        return render(request, 'gfx/userpacks/alluserp.html', {'userp': userp, 'products': products})

def PaidPacks(request):
    paid = PaidPackCat.objects.all()
    PaidID = request.GET.get('paidpacks')
    if PaidID:
        products = PaidPack.objects.filter(category=PaidID).order_by('-date_uploaded')
        return render(request, 'gfx/paidpacks/paidpacks.html', {'paid': paid, 'products': products})
    else:
        products = PaidPack.objects.all().order_by('-views')
        return render(request, 'gfx/paidpacks/allpaid.html', {'paid': paid, 'products': products})


def AddFreePacks(request):
    if request.method == "POST":
        freeform = AddFreePackForm(request.POST, request.FILES)
        if freeform.is_valid() and request.user.is_superuser or request.user.is_staff:
            freeform = freeform.save(commit=False)
            freeform.user = request.user
            freeform.save()
            messages.success(request, f'successfully Uploaded the packs')
            return redirect('home')
        else:
            messages.info("Something is wrong, Try Again")
    else:
        freeform = AddFreePackForm()
    return render(request, "gfx/post/post.html", {'form': freeform})

def FreePacks(request):
    freep = FreePackCat.objects.all()
    FreeID = request.GET.get('warexdesigns')
    if FreeID:
        products = FreePack.objects.filter(category=FreeID).order_by('-date_uploaded')
        return render(request, 'gfx/freepacks/freepacks.html', {'freep': freep, 'products': products})
    else:
        products = FreePack.objects.all().order_by('-views')
        return render(request, 'gfx/freepacks/allfree.html', {'freep': freep, 'products': products})


def AddWarexDesigns(request):
    if request.method == "POST":
        warexform = AddWarexDesignForm(request.POST, request.FILES)
        if warexform.is_valid() and request.user.is_superuser or request.user.is_staff:
            warexform.save(commit=False)
            warexform.form = request.user
            warexform.save()
            messages.success(request, f'successfully Uploaded the packs')
            return redirect('home')
        else:
            messages.info("Something is wrong, Try Again")
    else:
        warexform = AddWarexDesignForm()
    return render(request, "gfx/post/post.html", {'form': warexform})

def WarexDesigns(request):
    warex = WarexDesignCat.objects.all()
    WarexID = request.GET.get('warexdesigns')
    if WarexID:
        products = WarexDesign.objects.filter(category=WarexID).order_by('-date_uploaded')
        return render(request, 'gfx/warexdesigns/warexdesigns.html', {'warex': warex, 'products': products})
    else:
        products = WarexDesign.objects.all().order_by('-views')
        return render(request, 'gfx/warexdesigns/allwarex.html', {'warex': warex, 'products': products})

def AddUserDesigns(request):
    if request.method == "POST":
        userform = AddUserProductForm(request.POST, request.FILES)
        if userform.is_valid():
            userdesigns = userform.save(commit=False)
            userdesigns.user = request.user
            userdesigns.save()
            messages.success(
                request, f'Successfully Added Your Design for verification, it will be automatically uploaded once verified')
        else:
            messages.info("Something is wrong, Try Again")
    else:
        userform = AddUserProductForm()
    return render(request, "gfx/post/post.html", {'form': userform})

def UserDesigns(request):
    userdesign = UserDesignCat.objects.all()
    UserID = request.GET.get('userdesigns')
    if UserID:
        products = UserDesign.objects.filter(category=UserID).order_by('-date_uploaded')
        return render(request, 'gfx/userdesigns/userdesigns.html', {'userdesign': userdesign, 'products': products})
    else:
        products = UserDesign.objects.all().order_by('-views')
        return render(request, 'gfx/userdesigns/alluserpost.html', {'userdesign': userdesign, 'products': products})

def editpost(request, id):
        obj= get_object_or_404(Product, id=id)
        
        form = AddFreePackForm(request.POST or None, instance= obj)
        context= {'form': form}

        if form.is_valid():
                obj= form.save(commit= False)

                obj.save()

                messages.success(request, "You successfully updated the post")

                context= {'form': form}

                return render(request, 'gfx/post/editpost.html', context)

        else:
                context= {'form': form,
                           'error': 'The form was not updated successfully. Please enter in a title and content'}
                return render(request,'gfx/post/editpost.html' , context)

def editpost2(request, id):
        obj= get_object_or_404(Product, id=id)
        
        form = AddWarexDesignForm(request.POST or None, instance= obj)
        context= {'form': form}

        if form.is_valid():
                obj= form.save(commit= False)

                obj.save()

                messages.success(request, "You successfully updated the post")

                context= {'form': form}

                return render(request, 'gfx/post/editpost.html', context)

        else:
                context= {'form': form,
                           'error': 'The form was not updated successfully. Please enter in a title and content'}
                return render(request,'gfx/post/editpost.html' , context)

def editpost3(request, id):
        obj= get_object_or_404(Product, id=id)
        
        form = AddUserDesigns(request.POST or None, instance= obj)
        context= {'form': form}

        if form.is_valid():
                obj= form.save(commit= False)

                obj.save()

                messages.success(request, "You successfully updated the post")

                context= {'form': form}

                return render(request, 'gfx/post/editpost.html', context)

        else:
                context= {'form': form,
                           'error': 'The form was not updated successfully. Please enter in a title and content'}
                return render(request,'gfx/post/editpost.html' , context)


def editpost4(request, id):
        obj= get_object_or_404(Product, id=id)
        
        form = AddPaidPackForm(request.POST or None, instance= obj)
        context= {'form': form}

        if form.is_valid():
                obj= form.save(commit= False)

                obj.save()

                messages.success(request, "You successfully updated the post")

                context= {'form': form}

                return render(request, 'gfx/post/editpost.html', context)

        else:
                context= {'form': form,
                           'error': 'The form was not updated successfully. Please enter in a title and content'}
                return render(request,'gfx/post/editpost.html' , context)

def editpost5(request, id):
        obj= get_object_or_404(Product, id=id)
        
        form = AddUserPackForm(request.POST or None, instance= obj)
        context= {'form': form}

        if form.is_valid():
                obj= form.save(commit= False)

                obj.save()

                messages.success(request, "You successfully updated the post")

                context= {'form': form}

                return render(request, 'gfx/post/editpost.html', context)

        else:
                context= {'form': form,
                           'error': 'The form was not updated successfully. Please enter in a title and content'}
                return render(request,'gfx/post/editpost.html' , context)


def editpost6(request, id):
        obj= get_object_or_404(Product, id=id)
        
        form = AddPartnersPackForm(request.POST or None, instance= obj)
        context= {'form': form}

        if form.is_valid():
                obj= form.save(commit= False)

                obj.save()

                messages.success(request, "You successfully updated the post")

                context= {'form': form}

                return render(request, 'gfx/post/editpost.html', context)

        else:
                context= {'form': form,
                           'error': 'The form was not updated successfully. Please enter in a title and content'}
                return render(request,'gfx/post/editpost.html' , context)



def AddPartnerPack(request):
    if request.method == "POST":
        partnerform = AddPartnersPackForm(request.POST, request.FILES)
        if partnerform.is_valid():
            partnerpack = partnerform.save(commit=False)
            partnerform.user = request.user
            partnerpack.save()
            messages.success(
                request, f'Successfully Added Your Design for verification, it will be automatically uploaded once verified')
        else:
            messages.info("Something is wrong, Try Again")
    else:
        partnerform = AddPartnersPackForm
    return render(request, "gfx/post/post.html", {'form': partnerform})


def partnerspack(request):
    partners = PartnersName.objects.all()
    YTPacksID = request.GET.get('ytpacks')
    if YTPacksID:
        product = PartnersPack.objects.filter(partner=YTPacksID).order_by('-date_uploaded')
        return render(request, 'gfx/ytpacks/ytpacks.html', {'partners': partners, 'product': product})
    else:
        product = PartnersPack.objects.all().order_by('-views')
        return render(request, 'gfx/ytpacks/allpacks.html', {'partners': partners, 'product': product})

def uploads(request):
    product = WarexDesign.objects.filter(user = request.user, is_deleted=False)
    product2 = UserDesign.objects.filter(user = request.user, is_deleted=False)
    product3 = FreePack.objects.filter(user = request.user, is_deleted=False)
    product4 = PaidPack.objects.filter(user = request.user, is_deleted=False)
    product5 = UserPack.objects.filter(user = request.user, is_deleted=False)
    product6 = PartnersPack.objects.filter(user=request.user,is_deleted=False)

    context = {'product': product, 'product2': product2, 'product3': product3, 'product4':product4, 'product5': product5, 'product6': product6}
    return render(request, "accounts/user_upload.html", context)