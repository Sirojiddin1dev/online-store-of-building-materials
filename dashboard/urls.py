from django.urls import path
from . import views

urlpatterns = [
    path('banner/', views.banner_view, name="index_url"),
    path('single-product/<int:pk>/', views.single_product, name="single_product_url"),
    path('shop/', views.shopping_view, name="shop_url"),
]