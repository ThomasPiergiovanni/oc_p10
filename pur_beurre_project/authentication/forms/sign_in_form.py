from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.utils.translation import gettext_lazy as _


class SignInForm(AuthenticationForm):
    """
    """
    username = forms.CharField(label="Email", widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': True}))
    password = forms.CharField(label="Mot de passe",widget=forms.PasswordInput(attrs={'class': 'form-control'}))