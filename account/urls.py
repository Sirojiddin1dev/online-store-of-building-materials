from django.urls import path
from .views import *

urlpatterns = [
    path('register/', create_user_view, name='register_url'),
    path('register-staff/', create_staff_user_view, name='staff_create_url'),
    path('login/', login_view, name='login_url'),
    path('my-profile/<int:pk>/', my_profile_view, name='my_profile_url'),
    path('logout/', logout_view, name='logout_url'),
]
