import requests
from django.shortcuts import render

from .models import Greeting
from .models import Person


# Create your views here.
# <<<---- Login Page Starts Here ---->>
def login(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        title = request.POST['title']
        session = request.session
        session["name"] = title
    return render(request, "login.html", {"session": session})

# <<<---- Login Page Ends Here ---->>

def quiz(request):
    q1 = {"question": "What is C?", "op1": "Language", "op2": "Alphabet", "op3": "Ascii character",
          "op4": "All of these", "correct": "a"}
    q2 = {"question": "Who developed Python Programming language?", "op1": "Wick van rossum", "op2": "Dennis Ritchie",
          "op3": "Guido van Rossum", "op4": "none", "correct": "c"}
    q3 = {"question": "Which of the following is the correct extension of the python file?", "op1": ".python",
          "op2": ".pl", "op3": ".py", "op4": ".p", "correct": "c"}
    q4 = {"question": "Who developed C programming language ?", "op1": "denies ritchies", "op2": "Guido van Rossum",
          "op3": "harsh", "op4": "none", "correct": "a"}
    q5 = {"question": "Django is  a ?", "op1": "Programming Language", "op2": "Framework",
          "op3": "Python Web Framework", "op4": "None", "correct": "c"}
    questions = [q1, q2, q3, q4, q5]
    questionno = 0
    givenanswer = ""
    correctanswer = ""
    result = ""
    totalmarks = 0

    if request.POST:
        givenanswer = request.POST["option"];
        questionno = int(request.POST["qno"])
        totalmarks = int(request.POST["totalmarks"])
        correctanswer = questions[questionno].get("correct")
        questionno += 1
        totalmarks += 1
        result = "Yes"
        if givenanswer != correctanswer:
            result = "No"
            totalmarks -= 1
        if questionno >= len(questions):
            return render(request, 'result.html', {"total": totalmarks})
    # return httpResponse('python quiz!')
    return render(request, "quiz.html",
                  {"question": questions[questionno], "showqno": questionno + 1, "qno": questionno,
                   "givenanswer": givenanswer,
                   "correctanswer": correctanswer,
                   "result": result,
                   "totalmarks": totalmarks})


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
