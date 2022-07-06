from enum import unique
from django.db import models

# Create your models here.

class books(models.Model):
    id=models.IntegerField(primary_key=True, null=False, unique=True)
    name=models.CharField(null=False,max_length=200)
    author=models.CharField(max_length=100)
    type=models.CharField(max_length=40)
    content=models.CharField(max_length=2000)
    img_url=models.ImageField()
    yt= models.DateTimeField(auto_now_add = True)
    
    

