from django.contrib import admin
from .models import movies, movie_shares, movie_list, movie_list_content

# Register your models here.

class movie_admin(admin.ModelAdmin):
    list_display=("id","name","director","type","actor","img_url","time","date","content","yt")
    search_fields=("name","director","type",)
    
class movie_shares_admin(admin.ModelAdmin):
    list_display=("id","photo","rate","comment","yt","hide","movie","user")
    search_fields=("id",)
    
class movie_list_admin(admin.ModelAdmin):
    list_display=("id","name","user","hide")
    search_fields=("user",)
    
class movie_list_content_admin(admin.ModelAdmin):
    list_display=("id","movie","movie_list_name")
    search_fields=("movie",)
    
admin.site.register(movies,movie_admin)
admin.site.register(movie_shares,movie_shares_admin)
admin.site.register(movie_list,movie_list_admin)
admin.site.register(movie_list_content,movie_list_content_admin)