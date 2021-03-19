from django.contrib.auth.forms import UserCreationForm          #used for login and register
from django.contrib import messages                             # flash message show krega ye 
from django.contrib.auth import authenticate,login,logout       #for login , logout , checking-user
from django.contrib.auth.decorators import login_required       #login k baghair ghussnai nhi degaa
from django.contrib.auth.models import Group
from .decorators import *
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
@unauthenticated_user
def loginpage(request):
    if request.method =='POST':
        username=request.POST.get('username')     #form mai username k input ka ye name set kai tha 
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:            # agr user database mai hai
            login(request,user) 
            return redirect('/')
        else:
            messages.info(request,'userame or password is incorrect')
    context={}
    return render(request,'tasks/login.html',context)


def register(request):
    form=createuserform()             # user form ka object bnaya hai takkay use krskain register,html mai forms.as_p ka mtlb usko paragraph mai set krna 
    if request.method=='POST':
        form=createuserform(request.POST)  #usercreation form ko costumize kia hai forms.py mai
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='costumer')
            user.groups.add(group)                          # create krte hi group mai add krdega
            username =form.cleaned_data.get('username')                 #form say data catch krnay keliye
            messages.success(request,'Account was created for    '+ username)
            return redirect('login')                                 #flash message login page pe show huga 
    context={'form':form}
    return render(request,'tasks/register.html',context)
    

def logoutuser(request):
    logout(request)
    return redirect('login')
