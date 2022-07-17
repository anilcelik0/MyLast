from django.contrib import admin
from .models import books, book_shares

# Register your models here.

class book_admin(admin.ModelAdmin):
    list_display=("id","name","author","type","content","img_url","yt")
    search_fields=("name","author","type",)
    
class book_shares_admin(admin.ModelAdmin):
    list_display=("id","photo","rate","comment","yt","hide","book","user")
    search_fields=("id",)
    
    
admin.site.register(books,book_admin)
admin.site.register(book_shares,book_shares_admin)