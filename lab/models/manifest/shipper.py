from django.db import models

class Shipper():
    name = models.CharField(
        unique=True,
        max_length=50)
    
    objects = models.Manager()
    
   
    def __str__(self):
        return self.name
    
    class Meta:
        app_label = 'lab'
        ordering=('name',)