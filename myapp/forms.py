from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,PasswordResetForm,SetPasswordForm
from django.utils.translation import gettext,gettext_lazy as _
from django.contrib.auth import password_validation
from django.contrib.auth.models import User
from django.forms import ModelForm




# contact form 

class CustomerAddress(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name','email','website','content','phoneNo']
        widgets = {
                'name': forms.TextInput(attrs={'class': 'form-control'}),
                'email': forms.EmailInput(attrs={'class': 'form-control'}),
                'website': forms.TextInput(attrs={'class': 'form-control'}),
                'content': forms.TextInput(attrs={'class': 'form-control'}),
                'phoneNo': forms.NumberInput(attrs={'class': 'form-control'}),
            }


class CheckoutAddressForm(forms.ModelForm):
    class Meta:
        model = CheckoutAddress
        fields = ['fname', 'lname', 'email', 'region', 'address', 'apartment', 'town', 'postcode', 'country', 'phoneNo', 'OrderNote']
        labels = {'fname': 'First Name', 'lname': 'Last Name', 'email': 'Email Address', 'region': 'Region *', 'address': 'Street Address',
                  'apartment': 'Apartment', 'town': 'Town', 'postcode': 'Postcode', 'country': 'Country', 'phoneNo': 'Phone Number', 'OrderNote': 'Order Note'}

        widgets = {
            'fname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'lname': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'autocomplete': 'email', 'class': 'form-control', 'placeholder': 'abc@gmail.com'}),
            'region': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Region *'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Street Address *'}),
            'apartment': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apartment, suite, unit, etc. (optional)'}),
            'town': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Town / City *'}),
            'postcode': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Postcode *'}),
            'country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Country (optional)'}),
            'phoneNo': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number *'}),
            'OrderNote': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Order Note (optional)'}),
        }


# Forget Password 

class MyPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label=_("Email"),max_length=254,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control','placeholder':'Enter your email'}))

    class Meta:
        model = User
        fields = ['email']
        labels = {'email':'Email'}

# login form

class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    password = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control','placeholder':'Password'}))

    class Meta:
        model = User 
        fields = ['password1','username']
       

# sign up  

class CustomerRegistrationForms(UserCreationForm):
    password1 = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}))
    password2 = forms.CharField(label='Confirm Password',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'}))
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Email'}))
    username = forms.CharField(label=_("Username"),max_length=254,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Username'}))
    shipping_address_form = CheckoutAddressForm() 

    class Meta:
        model = User 
        fields = ['username','email','password1','password2']
        labels = {'email':'Email'}
