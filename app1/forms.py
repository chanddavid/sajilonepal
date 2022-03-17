
from dataclasses import field
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth import password_validation
from .models import Customer


class UserProfile(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'city', 'provience', 'post_code']
        labels={
            'name':'Name',
            'city':'City',
            'provience':'Provience',
            'post_code':'Post Code'
        }
        widgets={
            'name':forms.TextInput(attrs={'class': 'form-control'}),
            'city':forms.TextInput(attrs={'class': 'form-control'}),
            'provience':forms.Select(attrs={'class': 'form-control'}),
            'post_code':forms.NumberInput(attrs={'class': 'form-control'}),
        }


class RegisterForm(UserCreationForm):
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        render_value=True, attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        render_value=True, attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'email']
        labels = {
            'email': 'Email'
        }
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control '}),
            'last_name': forms.TextInput(attrs={'class': 'form-control '}),
            'email': forms.EmailInput(attrs={'class': 'form-control '}),
        }


class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'autofocus': True}))
    password = forms.CharField(label=_("Password"), strip=False, widget=forms.PasswordInput(
        render_value=True, attrs={'class': 'form-control', 'autocomplete': 'current-password'}))


class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old Password"), widget=forms.TextInput(
        attrs={'class': 'form-control', 'autofocus': True}))

    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(
        render_value=True, attrs={'class': 'form-control', 'autocomplete': 'new-password'}), help_text=password_validation.password_validators_help_text_html())

    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(
        render_value=True, attrs={'class': 'form-control', 'autocomplete': 'new-password'}))


class MyResetPasswordForm(PasswordResetForm):
    email = forms.EmailField(label=_("Emails"), max_length=254, widget=forms.EmailInput(
        attrs={'autocomplete': 'email', 'class': 'form-control'}))


class MyResetNewPasswordForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_("New Password"), strip=False, widget=forms.PasswordInput(
        render_value=True, attrs={'class': 'form-control', 'autocomplete': 'new-password'}), help_text=password_validation.password_validators_help_text_html())

    new_password2 = forms.CharField(label=_("Confirm New Password"), strip=False, widget=forms.PasswordInput(
        render_value=True, attrs={'class': 'form-control', 'autocomplete': 'new-password'}))
