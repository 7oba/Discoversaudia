from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm,UserCreationForm)

from .models import Profile

from datetime import date,timedelta
import datetime

#username here is email because we make username field in Profile USer as Email
class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(widget=forms.EmailInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'login-username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))



class Dateinput(forms.DateInput):
    input_type='date'


class RegistrationForm(forms.ModelForm):

    name = forms.CharField(
        label='Enter Username', min_length=4, max_length=50, help_text='Required')
    email = forms.EmailField(max_length=100, help_text='Required', error_messages={
        'required': 'Sorry, you will need an email'})
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput)
   
   

    date_of_birth=forms.DateField(label=" Date of Birth",required=True, help_text='Required',error_messages={
         'required': 'Sorry, you will need Birth Date'},widget=Dateinput)
    profile_img = forms.ImageField(label='Profile Image',required=False,widget=forms.ClearableFileInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Profile Image'}))
    
    class Meta:
        model = Profile
        fields = ('name', 'email','profile_img')

    def clean_username(self):
        name = self.cleaned_data['name'].lower()
        r = Profile.objects.filter(name=name)
        if r.count():
            raise forms.ValidationError("Username already exists")
        return name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords do not match.')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if Profile.objects.filter(email=email).exists():
            raise forms.ValidationError(
                'Please use another Email, that is already taken')
        return email
    

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})
        self.fields['date_of_birth'].widget.attrs.update(
            {'class': 'form-control'})



class UserEditForm(forms.ModelForm):

    email = forms.EmailField(
        label='Account email (can not be changed)', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3 bg-light', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))

    # user_name = forms.CharField(
    #     label='Firstname', min_length=4, max_length=50, widget=forms.TextInput(
    #         attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'form-firstname', 'readonly': 'readonly'}))

    name = forms.CharField(
        label='name', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Your name', 'id': 'form-lastname'}))

    date_of_birth = forms.DateField(
        label='Birth Date', widget=Dateinput(attrs={'class': 'form-control mb-3', 'placeholder': 'birthdate'}))
    profile_img = forms.ImageField(
        label='Profile Image',required=False,widget=forms.ClearableFileInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Profile Image'}))


    class Meta:
        model = Profile
        fields = ('email','name','date_of_birth','profile_img')



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['user_name'].required = True
        self.fields['email'].required = True
