# from curses.ascii import HT
from django.shortcuts import render,redirect
from .forms import * 
from django.views.generic.base import View, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User 
from .models import *
from django.contrib.auth import authenticate,logout,login
import string, random,os
from django.core.files.storage import FileSystemStorage
from wsgiref.util import FileWrapper


# Create your views here.
class ChannelView(View):
    def get(self, request, id):
        if request.user.is_authenticated:
            print(Channel.objects.get().channel_name)
            #
            # print(user)
            # print(user)
            videos = Video.objects.filter(id=id).order_by("-datetime")
            print(videos)
            # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            # video_path = 'http://localhost:8000/get_video/'+videos.path
            # print(videos)
            # print(Channel.objects.filter(id =id).get())
            
            return render(request, 'channelview.html', {'channel':Channel.objects.filter(id=id).get(), 'videos': videos})
           
class VideoView(View):
    def get(self,request,id):
        video_by_id=Video.objects.get(id=id)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        video_by_id.path = 'http://localhost:8000/get_video/'+video_by_id.path
        print(video_by_id)
        print(video_by_id.path)

        context = {'video':video_by_id}
        
        if request.user.is_authenticated:
            print('user signed in')
            comment_form = CommentForm()
            context['form'] = comment_form

        
        comments = Comment.objects.filter(video__id=id).order_by('-datetime')[:5]
        print(comments)
        context['comments'] = comments

        try:
            channel = Channel.objects.filter(user__username = request.user).get().channel_name != ""
            print(channel)
            context['channel'] = channel
        except Channel.DoesNotExist:
            channel = False

        return render(request, 'video.html', context)
class VideoFile(View):
    def get(self,request,file_name):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print("HELLO")
        print(BASE_DIR)
        print(file_name)
        file = FileWrapper(open(BASE_DIR+'/youtube/static/videos/'+file_name, 'rb'))
        response = HttpResponse(file, content_type='video/mp4')
        response['Content-Disposition'] = 'attachment; filename={}'.format(file_name)
        return response

class Login(View):
     
    def get(self, request):
        if request.user.is_authenticated:
            #logout(request)
            return redirect('home')

        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    def post(self, request):
        # pass filled out HTML-Form from View to LoginForm()
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # create a new entry in table 'logs'
                login(request, user)
                print('success login')
                return redirect('/')
            else:
                return redirect('login')
       

class CreateChannel(View):
    def get(self,request):
        if request.user.is_authenticated:
            try:
                if Channel.objects.filter(user=request.user).get().channel_name!='':
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
        print(most_recent_videos)
        most_recent_channels = Channel.objects.filter()
        channel=False 
        if request.user.username!="":
            try:
               channel=Channel.objects.filter(user=request.user)
               print(channel)
            except Channel.DoesNotExist:
               channel=False  
        print('home')
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
class comment(View):
    def get(self,request):
        form=CommentForm(request.POST)
        if form.is_valid():
            text=form.cleaned_data['text']
            video_id=request.POST['video']
            video=Video.objects.get(id=video_id)
            new_comment = Comment(text=text, user=request.user, video=video)
            new_comment.save()
            return render('/video/{}'.format(str(video_id)))


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
class Logout(View): 
    def get(self,request):
        logout(request)
        return redirect('home')
class NewVideo(View):
    def get(self,request):
        if request.user.is_authenticated ==False:
           return redirect('register')
        try:
            channel=Channel.objects.filter(user=request.user).get().channel_name!='' 
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