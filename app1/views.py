from django.shortcuts import render
from .forms import * 
from django.contrib.auth.models import User 
from .models import *
from django.contrib.auth import authenticate,logout,login







# Create your views here.
def home(request):
    return render(request,'index.html')