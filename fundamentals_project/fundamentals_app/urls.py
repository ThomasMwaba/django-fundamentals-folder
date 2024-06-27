from django.urls import path

from . import views # . because they are in the same directory

urlpatterns = [
    path('',views.home,name='home'), # This is the main page of the site
    path('planet-list',views.planet_async,name='planet-list'),
]

