from django import forms 

class LoginForm(forms.Form):
    username=forms.charField(label='Username',max_length=20)
    password=forms.charField(label='password',max_length=20,widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username=forms.CharField(label='Usename',max_length=20)
    password=forms.CharField(label='password',max_length=20,widget=forms.PasswordInput)
    email=forms.CharField(label='Email',max_length=20, widget=forms.EmailInput)

