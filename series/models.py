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
    
    def __str__(self):
        return self.name
    
class series_shares(models.Model):
    id=models.IntegerField(primary_key=True, null=False, unique=True)
    photo=models.ImageField(upload_to='series/shares',null=True)
    comment=models.CharField(max_length=2000, null=False)
    yt=models.DateTimeField(auto_now_add = True)
    
    role_hide=[(0,'herkes'),
        (1,'gizli')]
    hide = models.IntegerField(null=False,choices=role_hide,default=0)
    
    role_rate=[(1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5')]
    rate = models.IntegerField(null=False,choices=role_rate,default=1)
     
    series=models.ForeignKey(to='series.seriess', on_delete=models.CASCADE, related_name='series_share', null=False)
    user=models.ForeignKey(to='auth.User', on_delete=models.CASCADE, related_name='series_user', null=False)
    
