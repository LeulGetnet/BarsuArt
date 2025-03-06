from django import forms
from .models import Order
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV3
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user_name', 'description', 'sample_photo', 'wanted_size', 'style', 'email_or_phone_number']
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control custom-input',
                'placeholder': 'Describe your desire',
            }
        )
    )
    sample_photo = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control custom-file-input'}),
    )
    wanted_size = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control custom-input', 'placeholder': 'E.g., 40x30 CM'}),
    )
    style = forms.ChoiceField(
    choices=[('detailed', 'Detailed'), ('abstract', 'Abstract')],
    widget=forms.Select(attrs={'class': 'form-select custom-select'}),
    )

    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Your prefered calling name'}),
    )
    email_or_phone_number = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control custom-input', 'placeholder': 'Your email or phone number'}),
    )
    captcha = ReCaptchaField(widget=ReCaptchaV3())