from django.urls import path
from book import views

# http://127.0.0.1:8000/

urlpatterns = [
    path('', views.index, name='book'),
    path('book_page/<str:book_name>', views.book_page, name="page")
]