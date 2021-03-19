from django.shortcuts import render
from .models import *
import datetime
from django.http import JsonResponse
import json
# Create your views here.
from django.views.decorators.csrf import csrf_exempt,csrf_protect
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
from django.contrib.auth.decorators import login_required       #login k baghair ghussnai nhi degaa


@csrf_protect
@login_required(login_url='login')
def store(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        Order,customer=order.objects.get_or_create(customer=customer,complete=False)  # kahli wo order ju complete nhi huey us customer kay
        items=Order.orderitems_set.all()
        cartitems=Order.get_cart_items
    else:
        items=[]
        Order={"get_cart_total":0,"get_cart_items":0}
        cartitems=Order['get_cart_items']

    products=product.objects.all()
    context={"products":products, 'cartitems':cartitems,'shipping':False}
    return render(request,'store/store.html',context)


def cart(request):
    if request.user.is_authenticated:
        customer=request.user.customer
        Order,customer=order.objects.get_or_create(customer=customer,complete=False)  # kahli wo order ju complete nhi huey us customer kay
        items=Order.orderitems_set.all()
        cartitems=Order.get_cart_items
    else:
        items=[]
        Order={"get_cart_total":0,"get_cart_items":0}
        cartitems=Order['get_cart_items']

    context={'items':items ,'Order':Order,"cartitems":cartitems,'shipping':False}
    return render(request,'store/cart.html',context)

@csrf_exempt
def checkout(request):   
    if request.user.is_authenticated:
        customer=request.user.customer
        Order,customer=order.objects.get_or_create(customer=customer,complete=False)  # kahli wo order ju complete nhi huey us customer kay
        items=Order.orderitems_set.all()
        cartitems=Order.get_cart_items
    else:
        items=[]
        Order={"get_cart_total":0,"get_cart_items":0,'shipping':False}
        cartitems=Order["get_cart_items"]
    print(items)
    context={'items':items ,'Order':Order,'cartitems':cartitems}
    return render(request,'store/checkout.html',context)


def updateitem(request):   
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)
    customer=request.user.customer
    Product = product.objects.get(id=productId)
    Order,craeted=order.objects.get_or_create(customer=customer,complete=False)
    Orderitems, created= orderitems.objects.get_or_create(order=Order,product=Product)
    
    if action=="add":
        Orderitems.quantity=Orderitems.quantity+1
    elif action=="remove":
        Orderitems.quantity=Orderitems.quantity-1
    Orderitems.save()

    if Orderitems.quantity<=0:
        Orderitems.delete()

    return JsonResponse('ItemWasAdded',safe=False)

@csrf_exempt
def processorder(request):
    transcation_id=datetime.datetime.now().timestamp()
    data =json.loads(request.body)
    if request.user.is_authenticated:
        customer=request.user.customer
        Order,created=order.objects.get_or_create(customer=customer,complete=False)
        total=float(data['form']['total'])    # fetching from submitformdata in checkout.html
        order.transaction_id=transcation_id

        if total==Order.get_cart_total:
            Order.complete=True
            Order.save()

        if Order.shipping==True:
            shippingaddress.objects.create(
                customer=customer,
                order=Order,
                address=data['shipping']['address'],
                city = data['shipping']['city'],
                state=data['shipping']['state'],
                zip_code=data['shipping']['zipcode'],
            )
    else:
        print('user is not logged in...')
    return JsonResponse("payment Completed..",safe=False)





@csrf_protect
@unauthenticated_user   #---from decorators file
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
    return render(request,'store/login.html',context)


def register(request):
    form=createuserform()             # user form ka object bnaya hai takkay use krskain register,html mai forms.as_p ka mtlb usko paragraph mai set krna 
    if request.method=='POST':
        form=createuserform(request.POST)  #usercreation form ko costumize kia hai forms.py mai
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='customer')
            user.groups.add(group)                          # create krte hi group mai add krdega
            username =form.cleaned_data.get('username')                 #form say data catch krnay keliye
            messages.success(request,'Account was created for    '+ username)
            return redirect('login')                                 #flash message login page pe show huga 
    context={'form':form}
    return render(request,'store/register.html',context)
    

def logoutuser(request):
    logout(request)
    return redirect('login')
