from django.urls import path
from .views import *

urlpatterns = [
    path('about/', about_view, name='about_url'),
]
