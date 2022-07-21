# from curses.ascii import HT
from django.shortcuts import render,redirect
from .forms import * 
from django.views.generic.base import View, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User 
from .models import *
from django.contrib.auth import authenticate,logout,login
import string, random,os
from django.core.files.storage import FileSystemStorage


# Create your views here.

class CreateChannel(View):
    def get(self,request):
        if request.user.is_authenticated:
            try:
                if Channel.objects.filter(user__username=request.user).get().channel_name!='':
                    return redirect('home')
            except Channel.DoesNotExist:
                form=ChannelForm()
                channel=False 
                return render(request,'createchannel.html',{'form':form,'channel':channel})
    def post(self,request):
        form = ChannelForm(request.POST)
        if form.is_valid():
            # create a User account
            print(form.cleaned_data['channel_name'])
            channel_name = form.cleaned_data['channel_name']
            user = request.user
            subscribers = 0
            new_channel = Channel(channel_name=channel_name, user=user, subscribers=subscribers)
            new_channel.save()
            return redirect('home')
class home(View):
    def get(self,request):
        most_recent_videos = Video.objects.order_by('-datetime')[:8]
        most_recent_channels = Channel.objects.filter()
        channel=False 
        if request.user.username!="":
            try:
               channel=Channel.objecs.filter(user_username=request.user)
            except Channel.DoestnotExist:
               channel=False  
        return render(request,'home.html',{'menu_active_item':'home','most_recent_videos':most_recent_videos,'most_recent_channels':most_recent_channels,'channel':channel})
class Logout(View):
    def get(self,request):
        if request.user.is_authenticated:
           return redirect('home')
        form=LoginForm()
        return render(request,'login.html',{'form':form})
    def post(self,request):
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return redirect('login')
        # return 

class register(View):
    def get(self,request):
        if request.user.is_authenticated:
           return redirect('home')
        form=RegisterForm()
        return render(request,'register.html',{'form':form})
    def post(self,request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            # create a User account
            print(form.cleaned_data['username'])
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            new_user = User(username=username, email=email)
            new_user.set_password(password)
            new_user.save() 
            return redirect('login')
def logout(request):
    logout(request)
    return redirect('home')
class NewVideo(View):
    def get(self,request):
        if request.user.is_athenticated ==False:
           return redirect('register')
        try:
            channel=Channel.objects.filter(user__username=request.user).get().channel_name!='' 
            if channel:
               form=NewVideoForm() 
               return render(request,'new_video.html',{'form':form,'channel':channel})
        except Channel.DoesNotExist:
          return HttpResponseRedirect('/')
    def post(self,request):
        form=NewVideoForm(request.POST,request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            file = form.cleaned_data['file']
            
            random_char = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
            path=random_char+file.name 
            fs = FileSystemStorage(location = os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
            filename = fs.save("youtube/static/videos/"+path, file)
            file_url = fs.url(filename)
            new_video = Video(title=title, 
                            description=description,
                            user=request.user,
                            path=path)
            new_video.save()
            return redirect('/video/{}'.format(new_video.id))