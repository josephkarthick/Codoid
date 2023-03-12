from django.db import models

class codoid_login (models.Model):
    username        = models.CharField(max_length=50)
    email       = models.CharField(max_length=50)
    password    = models.CharField(max_length=50)
    
    
