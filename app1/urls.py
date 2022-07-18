from django.urls import path,include
from .views import *
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',index,name='index')
]
