from django.urls import path
from movie import views

# http://127.0.0.1:8000/

urlpatterns = [
    path('', views.index, name='movie'),
    path('page/<str:movie_name>', views.movie_page, name="movie_page"),
    path('movie_save', views.movie_save, name='movie_save')
]