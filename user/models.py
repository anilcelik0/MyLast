from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class profile_photo(models.Model):
    user=models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    pp=models.ImageField(upload_to='profile_photos', unique=True, default='fakepp.jpg')
    
    def __str__(self):
        return self.user.username

class follow_event(models.Model):
    id=models.IntegerField(primary_key=True, null=False, unique=True)
    following_user=models.ForeignKey(to='auth.User', on_delete=models.CASCADE, related_name='following_user', null=False)
    followed_user=models.ForeignKey(to='auth.User', on_delete=models.CASCADE, related_name='followed_user', null=False)
    yt=models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.following_user.username