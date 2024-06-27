from django.db import models

from django.utils.text import slugify



# Create your models here.


class Planet(models.Model):
    
    name = models.CharField(max_length=30) # planet name
    
    size = models.DecimalField(max_digits=6,decimal_places=2) #
    
    
    fact = models.CharField(max_length=100) # fact about the planet
    
    slug = models.SlugField(unique=True,blank=True)
    
    planets = models.Manager() # renaming the model manager 

 
    
    def save(self,*args,**kwargs):
        # allows to add some custom code before we save the planet
        
        # Make a slug from the name and put it in the slug field
        self.slug = slugify(self.name)
        
        super().save(*args,**kwargs) 
            # saves it             
    def __str__(self):
        
        return self.name
        # shows the Name of the Database
    
    

    
    
    
    
