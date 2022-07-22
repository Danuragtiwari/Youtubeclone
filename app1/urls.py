from django.contrib import admin
from django.urls import path
from .views import HomeView, NewVideo, CommentView, LoginView, RegisterView, VideoView, VideoFileView, LogoutView, CreateChannelView, ChannelView
from app1 import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view()),
    path('new_video', NewVideo.as_view()),
    path('video/<int:id>/<int:new>/', VideoView.as_view()),
    path('comment', CommentView.as_view()),
    path('get_video/<file_name>', VideoFileView.as_view()),
    path('logout', LogoutView.as_view()),
    path('createchannel', CreateChannelView.as_view()),
    path('<user>/channel', ChannelView.as_view()),
    path('video/<int:v_id>/<int:u_id>/like', views.video_like, name='video_like'),
    path('video/<int:v_id>/<int:u_id>/unlike', views.video_unlike, name='video_unlike'),
    path('video/<int:v_id>/<int:u_id>/dislike', views.video_dislike, name='video_dislike'),
    path('video/<int:v_id>/<int:u_id>/undislike', views.video_undislike, name='video_undislike'),
    path('liked/', views.liked_videos, name='liked_videos'),
    path('watch_history/', views.watch_history, name = 'watch_history'),
    path('trending/', views.trending, name='trending'),
    path('help/', views.help, name='help'),
    path('channel_subscribe/<int:c_id>/', views.channel_subscribe, name='channel_subscribe'),
    path('channel_unsubscribe/<int:c_id>/', views.channel_unsubscribe, name='channel_unsubscribe'),
    path('subscriptions/', views.subscriptions, name = 'subscriptions'),
    path('channels_list/', views.channels_list, name = 'channels_list'),
]
 
