from django.urls import path,include
from .views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('login',login,name='login'),
    path('logout',logout,name='logout'),
    path('register',register,name='register')
]
