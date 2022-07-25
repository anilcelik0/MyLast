from django.contrib import admin
from .models import seriess, series_shares, series_list, series_list_content

# Register your models here.

class series_admin(admin.ModelAdmin):
    list_display=("id","name","creater","type","actor","img_url","start_time","content","yt")
    search_fields=("name","creater","type",)

class series_shares_admin(admin.ModelAdmin):
    list_display=("id","photo","rate","comment","yt","hide","series","user")
    search_fields=("id",)

class series_list_admin(admin.ModelAdmin):
    list_display=("id","name","user","hide")
    search_fields=("user",)
    
class series_list_content_admin(admin.ModelAdmin):
    list_display=("id","series","series_list_name")
    search_fields=("series",)
    
admin.site.register(seriess,series_admin)
admin.site.register(series_shares,series_shares_admin)
admin.site.register(series_list,series_list_admin)
admin.site.register(series_list_content,series_list_content_admin)