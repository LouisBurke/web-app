from django.db import models

# Create your models here.
class todo(models.Model):
    name = models.CharField(max_length=100, unique=True) #Like a VARCHAR field
    description = models.TextField() #Like a TEXT field
    created = models.DateTimeField() #Like a DATETIME field
