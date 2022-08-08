import requests
from django.shortcuts import render

from .models import Greeting
from .models import Person


# Create your views here.
def quiz(request):

    q1={"question":"What is C?","op1":"Language","op2":"Alphabet","op3":"Ascii character","op4":"All of these"}
    q2={"question":"who developed python programming language?","op1":"wick van rossum","op2":"rasmus harsh","op3":"guido van Rossum","op4":"none"}
    q3={"question":"which of the following is the correct extension of the python file?","op1":".python","op2":".pl","op3":".py","op4":".p"}
    q4={"question":"who developed c programming language ?","op1":"denies ritchies","op2":"shubham","op3":"harsh","op4":"none"}
    questions=[q1,q2,q3,q4]
    questionno = 0
    if request.POST:
        questionno=request.POST["qno"]
        questionno+=1
    #return httpResponse('python quiz!')
    return render(request, "quiz.html",{"question":questions[questionno]})

def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")

def newbase(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "newindex.html")

def use(request):
    requests.get("https://google.com")
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


def db(request):
    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


def personentry(request):
    person = Person()
    person.name = "Champak"
    person.address = "Varanasi"
    person.age = 30
    person.save()

    persons = Person.objects.all()

    return render(request, "personenter.html", {"persons": persons})
