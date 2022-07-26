from django.db import models
from django.forms import ImageField

# Create your models here.

class books(models.Model):
    id=models.IntegerField(primary_key=True, null=False, unique=True)
    name=models.CharField(null=False,max_length=200)
    author=models.CharField(max_length=100)
    type=models.CharField(max_length=40)
    content=models.CharField(max_length=2000)
    img_url=models.ImageField()
    yt=models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name
    
    
class book_shares(models.Model):
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
     
    book=models.ForeignKey(to='book.books', on_delete=models.CASCADE, related_name='book_share', null=False)
    user=models.ForeignKey(to='auth.User', on_delete=models.CASCADE, related_name='book_user', null=False)
    
    def __str__(self):
        return self.book.name
    
class book_list(models.Model):
    id=models.IntegerField(primary_key=True, null=False, unique=True)
    name=models.CharField(null=False,max_length=200)
    yt=models.DateTimeField(auto_now_add = True)
    user=models.ForeignKey(to='auth.User', on_delete=models.CASCADE, related_name='book_list_user', null=False)
    role_hide=[(0,'herkes'),
        (1,'gizli')]
    hide = models.IntegerField(null=False,choices=role_hide,default=0)
    
    def __str__(self):
        return self.name

class book_list_content(models.Model):
    id=models.IntegerField(primary_key=True, null=False, unique=True)
    book=models.ForeignKey(to='book.books', on_delete=models.CASCADE, related_name='book', null=False)
    yt=models.DateTimeField(auto_now_add = True)
    book_list_name=models.ForeignKey(to='book.book_list', on_delete=models.CASCADE, related_name='book_list_name', null=False)
    
    def __str__(self):
        return self.book.name
    

class book_saves(models.Model):
    id=models.IntegerField(primary_key=True, null=False, unique=True)
    book_share=models.ForeignKey('book.book_shares', on_delete=models.CASCADE, related_name='book_share')
    user=models.ForeignKey(to='auth.User', on_delete=models.CASCADE, related_name='book_share_user', null=False)
    yt=models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.user.username
    
