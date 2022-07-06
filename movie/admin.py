from django.contrib import admin
from .models import movies

# Register your models here.

class movie_admin(admin.ModelAdmin):
    list_display=("id","name","director","type","actor","img_url","time","date","content","yt")
    search_fields=("name","director","type","content",)
    
    
admin.site.register(movies,movie_admin)