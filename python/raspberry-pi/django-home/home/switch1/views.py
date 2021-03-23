from django.shortcuts import render,HttpResponse
from gpiozero import LED
import time
light=LED(4)

# Create your views here.

def index(request):

    context={
        "first_name":"Faiz",
        "state":"ON"
    }
    return render(request,"switch1/index.html",context)

def on(request):
    light.on()           
    context={
        "first_name":"Faiz",
        "last_name":"Faiz",
        "state":"ON"
    }
    return render(request,"switch1/switch1.html",context)
    
def off(request):
    light.off()
    context={
        "first_name":"Faiz",
        "last_name":"Faiz",
        "state":"OFF"
        }
    return render(request,"switch1/switch1.html",context)
