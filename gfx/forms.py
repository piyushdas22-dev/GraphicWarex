from django import forms
from .models import FreePack, FreePackCat, PaidPack, PaidPackCat, Product, UserDesign, UserPack, UserPackCat, WarexDesign, WarexDesignCat, UserDesignCat
from .choices import *
from django.contrib.auth.models import User


class AddUserProductForm(forms.ModelForm):
    user = forms.ModelChoiceField(label="",
                                  queryset=User.objects.all(),
                                  widget=forms.HiddenInput(), required=False)
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    details = forms.CharField(label='Description', widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    image = forms.FileField(label='Thumbnail', widget=forms.FileInput(
        attrs={'class': 'form-control'}))
    sp = forms.IntegerField(label='Selling Price', widget=forms.NumberInput(
        attrs={'class': 'form-control'}))
    dp = forms.IntegerField(label='Discounted Price', widget=forms.NumberInput(
        attrs={'class': 'form-control'}))
    download_link = forms.CharField(
        label='Order Link ( i.e Your Instagram handle Link )', widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(label="Category", queryset=UserDesignCat.objects.all(), required=True)

    class Meta:
        model = UserDesign
        fields = ['user', 'title', 'details', 'image',
                  'sp', 'dp', 'download_link', 'category']

class AddUserPackForm(forms.ModelForm):
    user = forms.ModelChoiceField(label="",
                                  queryset=User.objects.all(),
                                  widget=forms.HiddenInput(), required=False)
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    details = forms.CharField(label='Description', widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    image = forms.FileField(label='Thumbnail', widget=forms.FileInput(
        attrs={'class': 'form-control'}))
    sp = forms.IntegerField(label='Selling Price', widget=forms.NumberInput(
        attrs={'class': 'form-control'}))
    dp = forms.IntegerField(label='Discounted Price', widget=forms.NumberInput(
        attrs={'class': 'form-control'}))
    download_link = forms.CharField(
        label='Order Link ( i.e Your Instagram handle Link )', widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(label="Category", queryset=UserPackCat.objects.all(), required=True)

    class Meta:
        model = UserPack
        fields = ['user', 'title', 'details', 'image',
                  'sp', 'dp', 'download_link', 'category']


class AddFreePackForm(forms.ModelForm):
    user = forms.ModelChoiceField(label="",
                                  queryset=User.objects.all(),
                                  widget=forms.HiddenInput(), required=False)
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    details = forms.CharField(label='Description', widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    image = forms.FileField(label='Thumbnail', widget=forms.FileInput(
        attrs={'class': 'form-control'}))
    download_link = forms.CharField(
        label='Download Link', widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(label="Category", queryset=FreePackCat.objects.all(), required=True)
    class Meta:
        model = FreePack
        fields = ['user','title', 'details', 'image', 'download_link', 'category']


class AddWarexDesignForm(forms.ModelForm):
    user = forms.ModelChoiceField(label="",
                                  queryset=User.objects.all(),
                                  widget=forms.HiddenInput(), required=False)
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    details = forms.CharField(label='Description', widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    image = forms.FileField(label='Thumbnail', widget=forms.FileInput(
        attrs={'class': 'form-control'}))
    sp = forms.IntegerField(label='Selling Price', widget=forms.NumberInput(
        attrs={'class': 'form-control'}))
    dp = forms.IntegerField(label='Discounted Price', widget=forms.NumberInput(
        attrs={'class': 'form-control'}))
    download_link = forms.CharField(
        label='Download Link', widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(label="Category", queryset=WarexDesignCat.objects.all(), required=True)

    class Meta:
        model = WarexDesign
        fields = ['user','title', 'details', 'image',
                  'sp', 'dp', 'download_link', 'category']


class AddPaidPackForm(forms.ModelForm):
    user = forms.ModelChoiceField(label="",
                                  queryset=User.objects.all(),
                                  widget=forms.HiddenInput(), required=False)
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    details = forms.CharField(label='Description', widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    image = forms.FileField(label='Thumbnail', widget=forms.FileInput(
        attrs={'class': 'form-control'}))
    sp = forms.IntegerField(label='Selling Price', widget=forms.NumberInput(
        attrs={'class': 'form-control'}))
    dp = forms.IntegerField(label='Discounted Price', widget=forms.NumberInput(
        attrs={'class': 'form-control'}))
    download_link = forms.CharField(
        label='Download Link', widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ModelChoiceField(label="Category", queryset=PaidPackCat.objects.all(), required=True)
    class Meta:
        model = PaidPack
        fields = ['user','title', 'details', 'image',
                  'sp', 'dp', 'download_link', 'category']
