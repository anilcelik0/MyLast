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
    
    def __str__(self):
        return self.name
    
    
class movie_shares(models.Model):
    id=models.IntegerField(primary_key=True, null=False, unique=True)
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
     
    movie=models.ForeignKey(to='movie.movies', on_delete=models.CASCADE, related_name='movie_share', null=False)
    user=models.ForeignKey(to='auth.User', on_delete=models.CASCADE, related_name='movie_user', null=False)
    
    def __str__(self):
        return self.movie.name
    
class movie_list(models.Model):
    id=models.IntegerField(primary_key=True, null=False, unique=True)
    name=models.CharField(null=False,max_length=200)
    yt=models.DateTimeField(auto_now_add = True)
    user=models.ForeignKey(to='auth.User', on_delete=models.CASCADE, related_name='movie_list_user', null=False)
    role_hide=[(0,'herkes'),
        (1,'gizli')]
    hide = models.IntegerField(null=False,choices=role_hide,default=0)
    
    def __str__(self):
        return self.name

class movie_list_content(models.Model):
    id=models.IntegerField(primary_key=True, null=False, unique=True)
    movie=models.ForeignKey(to='movie.movies', on_delete=models.CASCADE, related_name='movie', null=False)
    yt=models.DateTimeField(auto_now_add = True)
    movie_list_name=models.ForeignKey(to='movie.movie_list', on_delete=models.CASCADE, related_name='movie_list_name', null=False)

    def __str__(self):
        return self.movie.name
    
class movie_saves(models.Model):
    id=models.IntegerField(primary_key=True, null=False, unique=True)
    movie_share=models.ForeignKey('movie.movie_shares', on_delete=models.CASCADE, related_name='movie_share')
    user=models.ForeignKey(to='auth.User', on_delete=models.CASCADE, related_name='movie_share_user', null=False)
    yt=models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.user.username
