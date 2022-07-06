from django.db import models

# Create your models here.

class movies(models.Model):
    id=models.IntegerField(primary_key=True, unique=True, null=False)
    name=models.CharField(null=False,max_length=200)
    director=models.CharField(max_length=100) #birden fazla olabilir, araya işaret koy
    type=models.CharField(max_length=60)
    actor=models.CharField(max_length=300) #birden fazla olabilir, araya işaret koy
    img_url=models.ImageField()
    time=models.CharField(max_length=30)
    date=models.CharField(max_length=40)
    content=models.CharField(max_length=2000)
    yt= models.DateTimeField(auto_now_add = True)

