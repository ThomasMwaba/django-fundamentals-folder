from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('This is the homepage') # This shows the homepage message

def blog(request):
    return HttpResponse('This is the blog page') # This shows the blog page message
