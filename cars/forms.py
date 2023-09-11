from django import forms
from django.forms import ModelForm
from captcha.fields import CaptchaField
from .models import Enquiry, TestDrive

class TestDriveForm(ModelForm):
    class Meta:
        model = TestDrive
        fields = ("car", "name", "email", "address", "phoneNumber", "date")
        widgets = {
            'car': forms.Select(attrs={'class': 'form-control',}),
            'name': forms.TextInput(attrs={'class':'form-control'}), 
            'email': forms.EmailInput(attrs={'class':'form-control'}), 
            'address': forms.TextInput(attrs={'class':'form-control'}), 
            'phoneNumber': forms.TextInput(attrs={'class':'form-control'}), 
            'date': forms.DateInput(attrs={'class':'form-control', 'type': 'date'})
        }

class EnquiryForm(ModelForm):
    captcha = CaptchaField(error_messages = {'invalid': 'Invalid CAPTCHA'})
    class Meta:
        model = Enquiry
        fields = ("name", "email", "address", "phoneNumber", "remarks")
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}), 
            'email': forms.EmailInput(attrs={'class':'form-control'}), 
            'address': forms.TextInput(attrs={'class':'form-control'}), 
            'phoneNumber': forms.TextInput(attrs={'class':'form-control'}), 
            'remarks': forms.TextInput(attrs={'class':'form-control'}), 
        }