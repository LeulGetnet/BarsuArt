from django import forms
from .models import Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
    name = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'custom-name', 'name': 'name', 'class': 'custom-contact-input', 'placeholder': 'Your name'}),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'id': 'custom-email', 'name': 'email', 'class': 'custom-contact-input', 'placeholder': 'Email'}),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'id': 'custom-message', 'name': 'message', 'class': 'custom-contact-textarea', 'placeholder': 'Your message..'}),
    )