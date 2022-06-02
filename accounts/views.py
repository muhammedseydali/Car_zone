

import re
from weakref import ref
from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
# Create your views here.
def register(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirmpassword = request.POST['confirm_password']

        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request,'Email already exists')
                    return redirect('register')   
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname,username=username,email=email,password=password)
                    auth.login(request, user)
                    messages.success(request, "you are logged in")
                    return redirect('dashboard')
                    user.save()     
                    messages.success(request,'You are registerd successfully')
                    return redirect('login')
        else:
            messages.error(request,'password does not match')
            return redirect('register')    

    return render(request,'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request, 'You are logged in')
            return redirect('dashboard')

        else:
            messages.error(request,'Invalid login credentials')
            return redirect('login')
    return render(request,'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are successfully loggedout!!')
        return redirect('home')
    return render(request,'accounts/logout.html')

def dashboard(request):
    
    return render(request,'accounts/dashboard.html')
