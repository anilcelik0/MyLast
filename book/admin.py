from django.contrib import admin
from .models import books, book_shares, book_list, book_list_content

# Register your models here.

class book_admin(admin.ModelAdmin):
    list_display=("id","name","author","type","content","img_url","yt")
    search_fields=("name","author","type",)
    
class book_shares_admin(admin.ModelAdmin):
    list_display=("id","photo","rate","comment","yt","hide","book","user")
    search_fields=("id",)
    
class book_list_admin(admin.ModelAdmin):
    list_display=("id","name","user","hide")
    search_fields=("user",)
    
class book_list_content_admin(admin.ModelAdmin):
    list_display=("id","book","book_list_name")
    search_fields=("book",)
    
admin.site.register(books,book_admin)
admin.site.register(book_shares,book_shares_admin)
admin.site.register(book_list,book_list_admin)
admin.site.register(book_list_content,book_list_content_admin)