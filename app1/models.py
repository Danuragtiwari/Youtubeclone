from django.db import models

# Create your models here.
class Video(models.Model):
    title=models.CharField(max_length=20)
    description=models.TextField(max_length=500)
    path=models.CarField(max_length=60)
    datetime=models.DateTimeField(auto_now=True,blank=False,null=False)
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)

class Comment(models.Model):
    text=models.TextField(max_length=400)
    user=models.ForeignKey('auth.user',on_delete=models.CASCADE)
    datetime=models.DateTimeField(auth_now=True,blank=False,null=False)
    video=models.ForeignKey(Video,on_dlete=models.CASCADE)

class Channel(models.Model):
    channel_name=models.CharField(max_length=50,blank=False,null=True)
    subscribers=models.IntegerField(defaut=0,blank=False,null=False)
    user=models.ForeignKey('auth.User',on_delete=models.CASCADE)