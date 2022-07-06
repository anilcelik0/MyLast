from django.db import models

# Create your models here.

class seriess(models.Model):
    id=models.IntegerField(primary_key=True, unique=True, null=False)
    name=models.CharField(null=False, max_length=200)
    creater=models.CharField(max_length=100) #birden fazla olabilir, araya işaret koy
    type=models.CharField(max_length=60)
    actor=models.CharField(max_length=300) #birden fazla olabilir, araya işaret koy
    img_url=models.ImageField()
    start_time=models.CharField(max_length=20)
    content=models.CharField(max_length=2000)
    yt= models.DateTimeField(auto_now_add = True)