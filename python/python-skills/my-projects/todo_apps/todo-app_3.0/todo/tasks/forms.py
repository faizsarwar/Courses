from django import forms
from django.forms import ModelForm

from django.contrib.auth.models import User               #for costimizig  user,registeration form
from django.contrib.auth.forms import UserCreationForm          #used for login and register
from .models import *
#forms automaticaly create hujaiga is say


#html mai hr form k andar csrf_token add krna huga form k andar wrna error aeyga
class taskform(forms.ModelForm):

    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Add new tasks....'})) # setting a placeholder in our form

    class Meta:     # we need to give at leasts two values

        model=tasks   # jis model keliye form banana hai wo, aur kiti fields rkhni hai form mai
        fields='__all__' 

        #is form ko apnay view mai import krwaoo aur
        # view say template mai bhejdo

class createuserform(UserCreationForm):   # adding email requiremnets in user creation form
    class Meta:
        model=User   # imported above
        fields=['email','username','password1','password2']  #khali whi ju hamain chaiye hain

class profileform(forms.ModelForm):
    class Meta:
        model=profile
        fields='__all__'
        exclude=['user']  #user update nhi krsktabs