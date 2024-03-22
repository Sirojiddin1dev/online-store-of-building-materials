from django.urls import path
from .views import *

urlpatterns = [
    path('index/', index_view, name='index_url'),
    path('blog/', blog_view, name='blog_url'),
    path('contact/', contact_view, name='contact_url'),
    path('sing-blog/<int:pk>/', single_blog_view, name='single_blog_url')
]
