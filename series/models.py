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
    comment=models.CharField(max_length=2000, null=False)
    like_count=models.IntegerField(default=0, null=False)
    yt=models.DateTimeField(auto_now_add = True)
    
    role_hide=[(0,'herkes'),
        (1,'gizli')]
    hide = models.IntegerField(null=False,choices=role_hide,default=0)
    
    role_rate=[(1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5')]
    rate = models.IntegerField(null=False,choices=role_rate,default=3)
     
    series=models.ForeignKey(to='series.seriess', on_delete=models.CASCADE, related_name='series_share', null=False)
    user=models.ForeignKey(to='auth.User', on_delete=models.CASCADE, related_name='series_user', null=False)
    
    def __str__(self):
        return self.series.name
    
class series_list(models.Model):
    id=models.IntegerField(primary_key=True, null=False, unique=True)
    name=models.CharField(null=False,max_length=200)
    yt=models.DateTimeField(auto_now_add = True)
    user=models.ForeignKey(to='auth.User', on_delete=models.CASCADE, related_name='series_list_user', null=False)
    role_hide=[(0,'herkes'),
        (1,'gizli')]
    hide = models.IntegerField(null=False,choices=role_hide,default=0)
    
    def __str__(self):
        return self.name

class series_list_content(models.Model):
    id=models.IntegerField(primary_key=True, null=False, unique=True)
    series=models.ForeignKey(to='series.seriess', on_delete=models.CASCADE, related_name='series', null=False)
    yt=models.DateTimeField(auto_now_add = True)
    series_list_name=models.ForeignKey(to='series.series_list', on_delete=models.CASCADE, related_name='series_list_name', null=False)

    def __str__(self):
        return self.series.name
    
class series_saves(models.Model):
    id=models.IntegerField(primary_key=True, null=False, unique=True)
    series_share=models.ForeignKey('series.series_shares', on_delete=models.CASCADE, related_name='series_share')
    user=models.ForeignKey(to='auth.User', on_delete=models.CASCADE, related_name='series_share_user', null=False)
    yt=models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.series_share.series.name
    
class series_share_liked(models.Model):
    id=models.IntegerField(primary_key=True, null=False, unique=True)
    series_share=models.ForeignKey('series.series_shares', on_delete=models.CASCADE, related_name='series_share_liked')
    user=models.ForeignKey(to='auth.User', on_delete=models.CASCADE, related_name='series_share_liked_user', null=False)
    yt=models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.series_share.series.name
