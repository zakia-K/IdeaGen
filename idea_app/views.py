from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.template import loader
from .models import Picture
import random

def home(request):
    return HttpResponse("Hi, This is my first django view!")
def hello_new(request):
    top_5_picture = Picture.objects.all()[:5]
    template = loader.get_template('idea_app/hello.html')
    context = {
        'top_5_picture': top_5_picture,
    }
    return HttpResponse(template.render(context, request))

def hello(request):
    return render(
            request,
            'idea_app/hello.html',
         )
    
def page2(request):
    all_pictures = Picture.objects.all()[:32]
    top_5_picture = random.sample(list(all_pictures), 5)
    template = loader.get_template('idea_app/page2.html')
    context = {
        'top_5_picture': top_5_picture,
    }
    return HttpResponse(template.render(context, request))

