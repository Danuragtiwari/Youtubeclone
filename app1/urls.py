from django.urls import path,include
from .views import *
# from django.views.generic.base import as_view
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',home.as_view(),name='home'),
    path('login',Login.as_view(),name='login'),
    path('logout',Logout.as_view(),name='logout'),
    path('register',register.as_view(),name='register'),
    path('new_video',NewVideo.as_view(),name='newvideo'),
    path('createchannel', CreateChannel.as_view(),name='createchannel'),
    path('comment',comment.as_view(),name='comment'),
    path('get_video/<file_name>', VideoFile.as_view(),name='VideoFile'),
    path("channel/<int:id>",ChannelView.as_view(),name='channelview'),
    path('video/<int:id>', VideoView.as_view(),name='videoview'),
    ]   
