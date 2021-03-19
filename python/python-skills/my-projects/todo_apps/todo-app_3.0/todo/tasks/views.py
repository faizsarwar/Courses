from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from .decorators import *
from django.contrib.auth.forms import UserCreationForm          #used for login and register
from django.contrib import messages                             # flash message show krega ye 
from django.contrib.auth import authenticate,login,logout       #for login , logout , checking-user
from django.contrib.auth.decorators import login_required       #login k baghair ghussnai nhi degaa
from django.contrib.auth.models import Group                    # group mai add krnay keliye user ko
from django.views.decorators.csrf import csrf_protect
from random import randint
from .filters import *
from django.core.mail import EmailMessage                       #for confirmation emails
from django.conf import settings                                #for confirmation emails
from django.template.loader import render_to_string             #for confirmation emails

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

@csrf_protect
def register(request):
    global form
    form=createuserform()             # user form ka object bnaya hai takkay use krskain register,html mai forms.as_p ka mtlb usko paragraph mai set krna 
    if request.method=='POST':
        form=createuserform(request.POST)  #usercreation form ko costumize kia hai forms.py mai
        if form.is_valid():
            global key
            key=randint(20,88)
            print('hey')
            print(key,'     key')
            return redirect('/confirm-account/{}'.format(key))
            #print('user created')
            #user=form.save()
            # using signals can also be done by below code
            #group=Group.objects.get(name='profile')
            #user.groups.add(group)                          # create krte hi group mai add krdega
            #profile.objects.create(user=user,name=user.username)
            print('profile created')
            username =form.cleaned_data.get('username')                 #form say data catch krnay keliye
            messages.success(request,'Account was created for    '+ username)
            #return redirect('account-created')                                 #flash message login page pe show huga 
    context={'form':form}
    return render(request,'tasks/register.html',context)
    

def logoutuser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@allowed_users(allowed_roles=['profile','staff','admin'])      
def userpage(request):
    tasks=request.user.profile.tasks_set.all()
    form=taskform()     # blank form
    if request.method=='POST':
        task=request.user.profile.tasks_set.create(title=request.POST)
        form=taskform(request.POST)     # us form mai post request ka data dalegaa 
        if form.is_valid():
           form.save()                     # us data ko save karega database mai
        return redirect('/')
    w=list(tasks)
    todotasks=[]
    taskword=[]
    for i in w:
        #print(i.id)
        #print(str(i).split(',')[1].split(':')[1])
        todoItem=str(i).split(',')[1].split(':')[1]
        todoItemWord=todoItem[3:-2]      # queryset mai say data fetch krnay keliye kia hai ye
        itemandkey=[]
        itemandkey.append(todoItemWord)
        taskword.append(todoItemWord)
        itemandkey.append(i.id)
        todotasks.append(itemandkey)
    #print(q)
    #print(str(w).split(',')[1].split(":")[1])
    #print(list(task))
    #print(task)
    #myfilter=todofilter(request.GET,queryset= tasks)      # for search form (see in filters.py)
    #print(myfilter)
    #tasks=myfilter.qs            # throw it in our context variable to see only searched results
    context={
        'todotasks':todotasks,
        'form':form,
    }
    return render(request,'tasks/user.html',context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['profile','staff','admin'])
def accountSettings(request):       #added-customer form 
    profile=request.user.profile
    form=profileform(instance=profile)
    if request.method=="POST":
        form=profileform(request.POST,request.FILES,instance=profile)
    if form.is_valid():
        form.save()
    context={'form':form}
    return render(request,"tasks/account-settings.html",context)      


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])                  #admin aur staff dono ko permission hugi
#@admin_only
def index(request):
    #task=request.user.profile.tasks_set.all()

    task=tasks.objects.all()
    form=taskform()     # blank form
    if request.method=='POST':
        task=request.user.profile.tasks_set.create(title=request.POST)

        #form=taskform(request.POST)     # us form mai post request ka data dalegaa 
        # if form.is_valid():
        #     form.save()                     # us data ko save karega database mai
        return redirect('/index/')
    context={
        'tasks': task,
        'form': form
    }
    return render(request,'tasks/lists.html',context)


@login_required(login_url='login')
def update_task(request,pk):
    task=tasks.objects.get(id=pk)
    form=taskform(instance=task)  #whi form huga bs usko edit krsktay hungay 
    context={'form':form}

    if request.method=='POST':
        form=taskform(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    return render(request,'tasks/update_tasks.html',context)


@login_required(login_url='login')
def delete(request,pk):
    item=tasks.objects.get(id=pk)
    todoItem=str(item).split(',')[1].split(':')[1][2:-2]
    if request.method=='POST':
        item.delete()
        return redirect('/')

    context={
        'item':todoItem
    }
    return render(request,'tasks/delete.html',context)


def confirm_account_email(request,key1):
    template=render_to_string('tasks/confirm-account-email.html',{'key1':key1})
    email=EmailMessage(
        'Please vreify your account',
        template,
        settings.EMAIL_HOST_USER,
        ['faizsarwar44@gmail.com'],        
        )
    email.fail_silently=False
    email.send()
    return render(request,'tasks/confirm-account.html')


def Account_created_email(request,key1):
    print(key)
    if int(key1)==key:
        template =render_to_string('tasks/account-created-email.html')   #ju email bhejni hai wo ismay likhengay 
        form.save()
        email=EmailMessage(
            'Account created successfully',          # subject
            template,                                # body
            settings.EMAIL_HOST_USER,                # is ka mtlb settings mai ju email set hai us say send krna hai
            ['faizsarwar44@gmail.com'],              # isko send krna hai 
        )
        email.fail_silently=False
        email.send()
        #profile=profile.objects.get(id=uid)
        #context={'profile':profile}
        return render(request,'tasks/account-created.html')
    else:
        return HttpResponse("Verification failed")


#filter use krnay keliye settings file mai imstalled apps k andar changes krni hungi