from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index_view, name='index_url'),
    path('blog/', blog_view, name='blog_url'),
    path('contact/', contact_view, name='contact_url'),
    path('sing-blog/<int:pk>/', single_blog_view, name='single_blog_url'),
    path('checkout/<int:pk>/', checkout_view, name='checkout_url'),
    path('cart/<int:id>/', cart_view, name='cart_url'),
    path('add_basket/<int:pk>/', add_basket, name='add_basket_url'),
    path('remove_cart_product/<int:pk>/', remove_cart_product, name='remove_cart_product_url'),
]
