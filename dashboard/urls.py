from django.urls import path
from . import views

urlpatterns = [
    path('banner/', views.banner_view, name = "index_url"),

]