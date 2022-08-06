from django.contrib import admin
from .models import follow_event, profile_photo

# Register your models here.

class follow_event_admin(admin.ModelAdmin):
    list_display=("id","following_user","followed_user","yt")
    search_fields=("following_user",)
    
class profile_photo_admin(admin.ModelAdmin):
    list_display=("user","pp")
    
admin.site.register(follow_event,follow_event_admin)
admin.site.register(profile_photo, profile_photo_admin)