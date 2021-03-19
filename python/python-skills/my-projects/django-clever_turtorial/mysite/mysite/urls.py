"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
     # jb bhi koii url add krengay tu jis url pe show krna hai ,include ka function lagana parayga(url with file path dengay) 
    path('admin/', admin.site.urls),
    path('polls/',include('polls.urls')),
    #hr app mai template k folder mai dobara app ka folder bana k tml bnaoo takay collision na hu
]

