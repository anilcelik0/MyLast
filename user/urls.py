from django.urls import path
from user import views

# http://127.0.0.1:8000/

urlpatterns = [
    path('logout/', views.logout, name= 'logout'),
    path('login/', views.login, name= 'login'),
    path('register/', views.register, name='register'),
]