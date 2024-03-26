from django.urls import path
from .views import *

urlpatterns = [
    path('admin-panel/', index_1_view, name='index_1_url'),
    path('create-product/', create_product, name='create_product'),
    path('update-product/<int:pk>/', update_product, name='update_product'),
    path('delete-product/<int:pk>/', delete_product, name='delete_product'),
    path('create-info/', info_create, name='create_info'),
    path('update-info/', info_update, name='update_info'),
    path('delete-info/', info_delete, name='delete_info'),
]