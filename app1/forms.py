from django import forms 

class LoginForm(forms.Form):
    username=forms.CharField(label='Username',max_length=20)
    password=forms.CharField(label='password',max_length=20,widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username=forms.CharField(label='Usename',max_length=20)
    password=forms.CharField(label='password',max_length=20,widget=forms.PasswordInput)
    email=forms.CharField(label='Email',max_length=20, widget=forms.EmailInput) 

class CommentForm(forms.Form):
    text=forms.CharField(label='text',max_length=300)

class NewVideoForm(forms.Form):
    title=forms.CharField(label='title',max_length=20)
    description=forms.CharField(label='description',max_length=300)
    file=forms.FileField()

class ChannelForm(forms.Form):
    channel_name=forms.CharField(label='channel',max_length=20)

