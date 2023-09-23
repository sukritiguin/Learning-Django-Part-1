from django.db import models

# Create your models here.

class Service(models.Model):
    service_icon = models.CharField(max_length=500)
    service_title = models.CharField(max_length=500)
    service_description = models.TextField()
    
    