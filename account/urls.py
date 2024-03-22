from django.urls import path
from .views import *

urlpatterns = [
    path('register/', create_user_view, name='register_url'),
    path('', login_view, name='login_url'),
    path('my-profile/', my_profile_view, name='my_profile_url'),
    path('account-details/', edit_user_view, name='account_details_url'),
    path('logout/', logout_view, name='logout_url'),
]
