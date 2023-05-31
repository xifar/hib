from django import forms
from . models import Enquiry

# This form is displayed on Contact page to get enquiry details 
# from customer.

class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name', 
                }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
                }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Contact No.',
                }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject',
                }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'message',
                'cols': '30',
                'rows': '7',
                'placeholder': 'Message',
                }),
        }