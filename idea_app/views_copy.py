from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request):
    return HttpResponse("Hi, This is my first django view!")
def hello(request):
    return render(
        request,
        'idea_app/hello.html',
    )
def page2(request):
    return render(
        request,
        'idea_app/page2.html',
        )
