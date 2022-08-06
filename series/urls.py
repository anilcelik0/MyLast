from django.urls import path
from series import views

# http://127.0.0.1:8000/

urlpatterns = [
    path('', views.index, name='series'),
    path('page/<str:series_name>', views.series_page, name="series_page"),
    path('series_save', views.series_save, name='series_save')
]