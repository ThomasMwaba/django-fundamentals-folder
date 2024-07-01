from django.shortcuts import render

import time, asyncio

from django.http import HttpResponse

from django.http import Http404


from fundamentals_app.models import Planet

from django.shortcuts import get_object_or_404



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


def planetlistview(request,id):
    
    try:
        planet = Planet.planets.get(id=id)
    except Planet.DoesNotExist:
       raise Http404(f"Planet {id} does not exist")
    
    context= {'planet':planet}
        
    return render(request,'planet-list.html',context=context)


# from django.http import Http404

# def planetlistview(request,id):
    
#     planet = get_object_or_404(Planet,id=id)
    
#     context = {'planet':planet}
    
#     return render(request,'planet-list.html',context=context)
    




    
    
    
    
    
    
    
    
