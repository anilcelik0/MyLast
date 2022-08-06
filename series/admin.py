from django.contrib import admin
from .models import seriess, series_shares, series_list, series_list_content, series_saves, series_share_liked

# Register your models here.

class series_admin(admin.ModelAdmin):
    list_display=("id","name","creater","type","actor","img_url","start_time","content","yt")
    search_fields=("name","creater","type",)

class series_shares_admin(admin.ModelAdmin):
    list_display=("id","rate","comment","yt","hide","series","user")
    search_fields=("id",)

class series_list_admin(admin.ModelAdmin):
    list_display=("id","name","user","hide")
    search_fields=("user",)
    
class series_list_content_admin(admin.ModelAdmin):
    list_display=("id","series","series_list_name")
    search_fields=("series",)
    
class series_saves_admin(admin.ModelAdmin):
    list_display=("id","series_share","user","yt")
    search_fields=("user",)
    
class series_share_liked_admin(admin.ModelAdmin):
    list_display=("id","series_share","user","yt")
    search_fields=("user","series_share")
    
admin.site.register(seriess,series_admin)
admin.site.register(series_shares,series_shares_admin)
admin.site.register(series_list,series_list_admin)
admin.site.register(series_list_content,series_list_content_admin)
admin.site.register(series_saves,series_saves_admin)
admin.site.register(series_share_liked,series_share_liked_admin)