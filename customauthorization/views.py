from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
# from django.contrib.auth.forms import AuthenticationForm
from customauthorization.forms import CustomUserCreationForm as UserCreationForm, CustomUserAuthenticationForm as AuthenticationForm
from django.contrib.auth import login

from django.contrib import messages
# from .models import CustomUser
from django.db import IntegrityError
# Create your views here.

def is_user_not_authenticated(user):
    return not user.is_authenticated

@user_passes_test(is_user_not_authenticated, login_url='homePage')
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)
            
            if user is not None:
                login(request , user)
                next_url = request.GET.get('next')
                if next_url:
                    return redirect(next_url)
                else:
                    return redirect('homePage')

        else:
            print(f'Error: {form.error_messages}')
            if form.error_messages:
                messages.error(request, 'Please enter a correct username and password.')
            # if form.error_messages
            context = {
                "form" : form  # Pass the existing form with errors
                }
            return render(request , 'user/login.html' , context=context )

    else:
        form = AuthenticationForm()
        return render(request, 'user/login.html', {'form': form})
    

def logout_view(request):
    logout(request)
    return redirect('loginPage')



@user_passes_test(is_user_not_authenticated, login_url='homePage')
def register_view(request):
    if request.method == 'GET':
        form = UserCreationForm()
        context = {
            "form" : form
        }
        return render(request , 'user/register.html' , context=context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)  
        context = {
            "form" : form
        }
        if form.is_valid():
            print("Registration form submitted!!")
            user = form.save()
            print(user)
            if user is not None:
                return redirect('loginPage')
        else:
           
            return render(request , 'user/register.html' , context=context)