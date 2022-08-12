from django.urls import path,include
from test1 import views
from django.contrib import admin

#TEMPLATE URLS

app_name = 'test1'

urlpatterns = [
    path('register/', views.register,name='register'),
    path('user_login/', views.user_login,name='user_login'),
]
