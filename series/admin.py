from django.contrib import admin
from .models import seriess

# Register your models here.

class series_admin(admin.ModelAdmin):
    list_display=("id","name","creater","type","actor","img_url","start_time","content","yt")
    search_fields=("name","creater","type","content",)
    
    
admin.site.register(seriess,series_admin)