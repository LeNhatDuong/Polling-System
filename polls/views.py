from django.http import HttpResponse
from .models import Question
from django.template import loader
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template("polls/index.html")
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))

def detail(resquest, question_id):
    return HttpResponse("You are looking at question {0}".format(question_id))

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response%question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s."% question_id)
