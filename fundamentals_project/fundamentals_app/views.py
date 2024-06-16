from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def home(request):
    planetlist = [
        
        {
           'name':'Mercury',
           'diameter':'4,879 km',
           'fact':'A year on Mercury takes 88 Earth days.',
           
        },
        
         {
           'name':'Venus',
           'diameter':'12,104 km',
           'fact':'Does not have any moons or rings.',
           
        },
        
    ] # list of data which will be shown on the webpage
    
    context = {'planetlist':planetlist} # prepares the data from driverlist to be displayed on index.html webpage
    return render(request,'index.html',context=context) # This shows the homepage message

def blog(request):
    return HttpResponse('This is the blog page') # This shows the blog page message
