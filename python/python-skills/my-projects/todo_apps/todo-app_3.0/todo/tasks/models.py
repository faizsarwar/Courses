from django.db import models
from django.contrib.auth.models import User


class profile(models.Model):                               # iskay singals file (mai iskay signls likhnay hungay )
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=200,null=True,blank=True)
    phone=models.CharField(max_length=200,null=True,blank=True)
    profile_pic=models.ImageField(null=True,blank=True,default='download.png')     #first run cammand pip install pillow, also add media root in settings file
  
    def __str__(self):
        return self.name


# Create your models here.
class tasks(models.Model):
    #user=models.OneToOneField(User,null=True,on_delete=models.CASCADE)          # har user ka alag task huga 
    profile=models.ForeignKey(profile,null=True,on_delete=models.SET_NULL)
    title=models.CharField(max_length=200)
    complete=models.BooleanField(default=False)
    created= models.DateTimeField(auto_now_add=True) #date khud add hujaigi krni nhi paraygi
    
    def __str__(self):
        return self.title

    