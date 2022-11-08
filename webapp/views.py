from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from .models import *

def home(request):
    datas = Resto.objects.all()
    return render(request, 'index.html', {'datas':datas})

def add_data(request):
    a = request.POST.get('name')
    a = Dataa(name=a)
    a.save()
    datas = Resto.objects.all()
    return render(request, 'index.html', {'datas':datas})

def register_form(request):
    return render(request, 'register.html')

def login_form(request):
    return render(request, 'login.html')

def loginuser(request):
    # code for login.
    username = request.POST.get('user')
    password = request.POST.get('pwd')

    u = authenticate(request, username=username, password=password)
    if u is not None:
        login(request, u)
        return render(request, 'login.html', {'msg':'You have successfuly logged in!', 'error':False})
    else:
        return render(request, 'login.html', {'msg':'Login failed! Please try again.', 'error':True})

def register(request):
    # code for registation.
    email = request.POST.get('email')
    username = request.POST.get('username')
    password1 = request.POST.get('pwd1')
    password2 = request.POST.get('pwd2')

    if password1==password2:
        user = User(username=username, email=email, password=password1)
        user.save()
        return render(request, 'register.html', {'message':'Registered successuly!', 'error':False})
    
    else:
        return render(request, 'register.html', {'message':"Password didn't match, please try again.", 'error':True})


def restaurant(request, slug, name):
        menu = item.objects.filter(hotel=name)
        desc = Resto.objects.get(slug=slug)
        com = Comments.objects.filter(hname=name)
        return render(request, 'rest_info.html', {'desc':desc, 'menu':menu, 'com':com})

def add_comment(request):
    comment = request.POST.get('comment')
    hname = request.POST.get('hname')
    a = Comments(hname=hname, comment=comment)
    a.save()
    datas = Resto.objects.all()
    return render(request, 'index.html', {'datas':datas})

def logoutuser(request):
    logout(request)
    return render(request, 'login.html')