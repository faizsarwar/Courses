from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from .models import todo
# Create your views here.
def index(request):   # saray items mai page pe show huay chiye isliye
    todo_items=todo.objects.all().order_by("-added_date")
    context={
        "todo_items":todo_items
    }
    return render(request,"todo/index.html",context)


@csrf_exempt
def add_todo(request):
    print(request.POST)
    current_date=timezone.now()
    content=request.POST["content"]
    print(content)
    print(current_date)
    todo.objects.create(added_date=current_date,text=content)
    return HttpResponseRedirect("/todo")

@csrf_exempt
def delete_todo(request,todo_id):
    todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect("/todo")

