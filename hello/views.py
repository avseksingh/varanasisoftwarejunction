import requests
from django.shortcuts import render

from .models import Greeting
from .models import Person


# Create your views here.
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
