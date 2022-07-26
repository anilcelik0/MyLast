from django.urls import path
from book import views

# http://127.0.0.1:8000/

urlpatterns = [
    path('', views.index, name='book'),
    path('page/<str:book_name>', views.book_page, name="book_page"),
    path('book_saves', views.book_saves, name='book_saves')
]