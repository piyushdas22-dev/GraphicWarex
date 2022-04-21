from django import forms
from .models import Product
from .choices import *


class AddUserDesignsForm(forms.ModelForm):
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
    order_link = forms.CharField(
        label='Instagram', widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(label='Category', choices=(('--', '------'),
        ('UDT', 'Thumbnail'),
                                                            ('UDB', 'Banner'),
                                                            ('UDI', 'Intro'),
                                                            ('UDO', 'Outro'),
                                                            ('UDP', 'Poster'),
                                                            ('UDOth', 'Other')), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ['title', 'details', 'image',
                  'sp', 'dp', 'order_link', 'category']


class AddUserPacksForm(forms.ModelForm):
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
    buy_link = forms.CharField(
        label='Buy Link ( i.e Instagram Link, Shorten Urls, Your Own Website Link Where Users can Buy This Pack, etc )', widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(label='Category', choices=(('--', '------'),
        ('UGT', 'Thumbnail'),
                                                            ('UGB', 'Banner'),
                                                            ('UGI', 'Intro'),
                                                            ('UGO', 'Outro'),
                                                            ('UGP', 'Poster'),
                                                            ('UGR', 'Render'),
                                                            ('UGG', 'GFX Materials')), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ['title', 'details', 'image',
                  'sp', 'dp', 'buy_link', 'category']


class AddFreePackForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    details = forms.CharField(label='Description', widget=forms.Textarea(
        attrs={'class': 'form-control'}))
    image = forms.FileField(label='Thumbnail', widget=forms.FileInput(
        attrs={'class': 'form-control'}))
    download_link = forms.CharField(
        label='Download Link', widget=forms.TextInput(attrs={'class': 'form-control'}))
    category = forms.ChoiceField(label='Category', choices=(('--', '------'),
        ('FPT', 'Thumbnail'),
                                                            ('FPB', 'Banner'),
                                                            ('FPI', 'Intro'),
                                                            ('FPO', 'Outro'),
                                                            ('FPP', 'Poster'),
                                                            ('FPR', 'Render'),
                                                            ('FPG', 'GFX Materials')), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ['title', 'details', 'image', 'download_link', 'category']


class AddNawabDesignsForm(forms.ModelForm):
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
    category = forms.ChoiceField(label='Category', choices=(('--', '------'),
        ('NT', 'Thumbnail'),
                                                            ('NB', 'Banner'),
                                                            ('NI', 'Intro'),
                                                            ('NO', 'Outro'),
                                                            ('NP', 'Poster'),
                                                            ('NOth', 'Other')), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ['title', 'details', 'image',
                  'sp', 'dp', 'download_link', 'category']


class AddPaidPackForm(forms.ModelForm):
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
    category = forms.ChoiceField(label='Category', choices=(('--', '------'),
        ('PPT', 'Thumbnail'),
                                                            ('PPB', 'Banner'),
                                                            ('PPI', 'Intro'),
                                                            ('PPO', 'Outro'),
                                                            ('PPP', 'Poster'),
                                                            ('PPR', 'Render'),
                                                            ('PPG', 'GFX Materials')), widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Product
        fields = ['title', 'details', 'image',
                  'sp', 'dp', 'download_link', 'category']
