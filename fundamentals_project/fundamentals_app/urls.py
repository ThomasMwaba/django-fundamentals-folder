from django.urls import path

from . import views # . because they are in the same directory

urlpatterns = [
    path('',views.home,name='home'), # This is the main page of the site
    path('blog',views.blog,name='blog'), # This is the blog page of the site
]