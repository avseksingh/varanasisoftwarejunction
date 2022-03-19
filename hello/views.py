from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from .models import Person

# Create your views here.
def index(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
def personentry(request):

    person = Person()
    person.save()

    persons = Person.objects.all()

    return render(request, "personenter.html", {"persons": persons})
