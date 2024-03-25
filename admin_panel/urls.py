from django.urls import path
from .views import *

urlpatterns = [
    path('admin-panel/', index_1_view, name='index_1_url'),
    path('create-product/', create_product, name='create_product'),
    path('info-create/', create_info, name='create_info'),
    path('blog-create/', create_blog, name='create_blog'),
]