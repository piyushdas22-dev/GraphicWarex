from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    content = forms.CharField(label='Your Issue', widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = Contact
        fields = ['email', 'content']
