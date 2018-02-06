from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import Http404
# Create your views here.
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request,'polls/index.html',context)

def detail(request, question_id):

    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404("Question does not exist")
    return HttpResponse("You're lookin at the question ID %s." % question_id)

def results(request, question_id):
    response =  "You're lookin at the results of question ID %s"
    return HttpResponse(response%question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on the question ID %s" % question_id)