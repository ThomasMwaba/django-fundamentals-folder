from django.db import models

# Create your models here.


class Planet(models.Model):
    
    name = models.CharField(max_length=30) # planet name
    
    size = models.DecimalField(max_digits=6,decimal_places=2) #
    
    
    fact = models.CharField(max_length=100) # fact about the planet
    
    
    
    def save(self,*args,**kwargs):
        # allows to add some custom code before we save the planet
            
            super().save(*args,**kwargs) 
            # saves it
       
            print(f'{self.name} has been added')
                        
                    # shows the name of the planet added               
    def __str__(self):
        
        return self.name
        # shows the Name of the Database
    
    

    
    
    
    
