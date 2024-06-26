from django.urls import path
from . import views

urlpatterns = [
    path('', views.banner_view, name="index_url"),
    path('single-product/<int:pk>/', views.single_product, name="single_product_url"),
    path('shop/', views.shopping_view, name="shop_url"),
    # Admin panel #
    path('all_product/', views.all_products, name="all_products_url"),
    path('all_info/', views.all_info, name="all_info_url"),
    path('all_checkout/', views.all_checkout, name="all_checkout_url"),
    path('all_banner/', views.all_banner, name="all_banner_url"),
    path('all_blog/', views.all_blog, name="all_blog_url"),
    path('all_contact/', views.all_contact, name="all_contact_url"),
]