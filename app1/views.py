# from curses.ascii import HT
from django.shortcuts import render,redirect
from .forms import * 
from django.views.generic.base import View, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User 
from .models import *
from django.contrib.auth import authenticate,logout,login



# Create your views here.

def home(request):
    most_recent_videos = Video.objects.order_by('-datetime')[:8]
    most_recent_channels = Channel.objects.filter()
    channel=False 
    if request.user.username!="":
        try:
            channel=Channel.objecs.filter(user_username=request.user)
        except Channel.DoestnotExist:
            channel=False  
    return render(request,'home.html',{'menu_active_item':'home','most_recent_videos':most_recent_videos,'most_recent_channels':most_recent_channels,'channel':channel})

def login(request):
    if request.user.is_authenticated:
         return redirect('home')
    form=LoginForm()
    return render(request,'login.html',{'form':form})
    

def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form=RegisterForm()
    return render(request,'register.html',{'form':form})
def logout(request):
    logout(request)
    return redirect('home')
