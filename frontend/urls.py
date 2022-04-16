from django.urls import path,include
from .views import *
urlpatterns = [

    path('',home),
    path('login/',login),
    path('signup/',signup)
]
