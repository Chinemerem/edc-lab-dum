from django.db import models 


class Consignee():
    
    name = models.CharField(
        unique=True,
        max_length=50,
        help_text='Company name')
    
    objects = models.Manager()
    
    def __str__(self):
        return self.name
    
    
    class Meta:
        app_label = 'lab'
        ordering =('name', )