from django.urls import path
from user import views

# http://127.0.0.1:8000/

urlpatterns = [
    path('logout/', views.logout, name= 'logout'),
    path('login/', views.login, name= 'login'),
    path('register/', views.register, name='register'),
    path('lists/', views.lists, name='lists'),
    path('profile/', views.profile, name='profile'),
    path('settings/', views.settings, name='settings'),
    path('profiles/<str:username>', views.profiles, name='profiles')
]