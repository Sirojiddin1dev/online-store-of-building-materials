from django.urls import path
from .views import *

urlpatterns = [
    path('admin-panel/', index_1_view, name='index_1_url'),
    path('create-product/', create_product, name='create_product'),
    path('update-product/<int:pk>/', update_product, name='update_product'),
    path('delete-product/<int:pk>/', delete_product, name='delete_product'),
    path('create-info/', info_create, name='create_info'),
    path('update-info/<int:pk>/', info_update, name='update_info'),
    path('delete-info/<int:pk>/', info_delete, name='delete_info'),
    path('create/', create_banner, name='create_banner'),
    path('update/<int:pk>/', update_banner, name='update_banner'),
    path('delete/<int:pk>/', delete_banner, name='delete_banner'),
    path('create-blog/', create_blog, name='create_blog'),
    path('update-blog/<int:pk>/', update_blog, name='update_blog'),
    path('delete-blog/<int:pk>/', delete_blog, name='delete_blog'),
]