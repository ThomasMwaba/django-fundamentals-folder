from django.shortcuts import render

import time, asyncio

from django.http import HttpResponse


from fundamentals_app.models import Planet

from asgiref.sync import sync_to_async


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


    
# @sync_to_async
# def planet1():
    
#     print('Getting planet one ...')
    
#     time.sleep(5)
    
#     planet1 = Planet.objects.get(id=1)
    
#     print(f'{planet1} has gotten')




# @sync_to_async
# def planet2():
    
#     print('Getting planet two ...')
    
#     time.sleep(5)
    
#     planet2 = Planet.objects.get(id=2)
    
#     print(f'{planet2} has gotten')



# async def planet_async(request):
    
#     print('Waiting to get planets')
    
#     planets = Planet.objects.all()
    
#     await asyncio.sleep(3)
    
#     print('Planets obtainted')

    
#     return HttpResponse(f'{planets} being displayed')



    
    
    
    
    
    
    
    
