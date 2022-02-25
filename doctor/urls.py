from django.contrib import admin
from django.urls import path
from doctor import views


urlpatterns = [
   path("",views.index,name='appointment'),
]

    