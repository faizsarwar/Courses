from django.shortcuts import render,get_object_or_404
from .models import Question
from django.http import HttpResponse,Http404  
from django.template import loader
# Create your views here.


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]    #error hai likn aasaee hai
    context = {
        'latest_question_list': latest_question_list,
    }
    return render(request,'polls/index.html',context)


# raising a 404 exception
def detail(request,question_id):   #using get_object_or_404 shortcut
    question1=get_object_or_404(Question,pk=question_id)

    return  render(request,"polls/details.html",{"question":question1})


def results(request,question_id):
    response='you are looking at the results of %s'
    return(HttpResponse(response % question_id))

def vote(request,question_id):
    return(HttpResponse("you're voting on qusetion {}".format(question_id)))