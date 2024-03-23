from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.shopping_view, name = "shop_url"),
    path('banner/', views.banner_view, name = "banner_url"),
    path('product1/', views.product1_view, name = "product1_url"),
    path('banner/', views.product2_view, name = "product2_url"),
    path('banner/', views.product3_view, name = "product3_view"),
    path('banner/', views.product4_view, name = "product4_url"),
    path('banner/', views.product5_view, name = "product5_view"),
]