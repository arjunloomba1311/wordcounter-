from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.Home,name = 'home'),
    path('/countingthewords',views.count,name = 'count'),
    path('/about',views.about,name = 'about'),
]
