from django.contrib import admin
from .models import books

# Register your models here.

class book_admin(admin.ModelAdmin):
    list_display=("id","name","author","type","content","img_url","yt")
    search_fields=("name","author","type","content",)
    
    
admin.site.register(books,book_admin)