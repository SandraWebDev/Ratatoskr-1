from django.shortcuts import render
from .models import Schedule, Timeslot
from django.http import HttpResponse

# Create your views here.

def schedule(request):
    html = "<html><body>Hello World.</body></html>" 
    return HttpResponse(html)