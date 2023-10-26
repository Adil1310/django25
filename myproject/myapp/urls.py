from django.urls import path
from .views import *

urlpatterns = [
    path('add/', add_icecream, name='add-icecream'),
    path('success/', success, name='success'),
]