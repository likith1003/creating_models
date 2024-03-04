from django.urls import path
from app.views import *

urlpatterns = [
    path('home', home, name='home'),
    path('login', login, name='login'),
    path('register', register, name='register')
]
