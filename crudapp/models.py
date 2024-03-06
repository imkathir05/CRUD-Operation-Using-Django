from django.db import models

# Create your models here.
class CRUD(models.Model):
    Name=models.CharField(max_length=30,default="")
    Age=models.IntegerField(max_length=40,default="")
    Address=models.CharField(max_length=30,default="")
    Phone=models.IntegerField(max_length=10,default="")
    
    