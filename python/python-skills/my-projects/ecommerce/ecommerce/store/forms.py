from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User               #for costimizig  user,registeration form
from django.contrib.auth.forms import UserCreationForm          #used for login and register
#forms automaticaly create hujaiga is say


# used for creating a user 
class createuserform(UserCreationForm):   # adding email requiremnets in user creation form
    class Meta:
        model=User   # iported above
        fields=['email','username','password1','password2']  #khali whi ju hamain chaiye hain