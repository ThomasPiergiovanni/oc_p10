from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from authentication.models import CustomUser
from authentication.forms import SignUpForm, SignInForm

# Create your views here.

def account(request):
    """
    """
    user = request.user
    if not user.is_authenticated:
        return redirect('authentication:sign_in')
    else:
        context = {
            'user':user
        }
        return render(request, 'authentication/account.html', context)     


def sign_up(request):
    """
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            user = CustomUser.objects.create_user(
                email=email,
                password=password1,
                first_name=first_name)
            return HttpResponseRedirect(reverse('authentication:sign_in'))
        else:
            context = {
                'form' : form
            }
            return render(request, 'authentication/sign_up.html', context)   
    else:
        form = SignUpForm()
        context = {
            'form' : form
        }
        return render(request, 'authentication/sign_up.html', context) 


def sign_in(request):
    """
    """
    if request.method == 'POST':
        form = SignInForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('supersub:index')
        else:
            context = {
                'form' : form
            }
            return render(request, 'authentication/sign_in.html', context)
    else:
        form = SignInForm()
        context = {
            'form' : form
        }
        return render(request, 'authentication/sign_in.html', context)

def sign_out(request):
    logout(request)
    return redirect('supersub:index') 