from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login, logout, authenticate


def create_user_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        img = request.FILES.get('img')
        User.objects.create_user(
            username=username,
            password=password,
            phone_number=phone_number,
            email=email,
            img=img
        )
        return redirect('login_url')
    return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request, usr)
            usr.update_login_info()  # Update login count and last login time
            if usr.is_superuser or usr.is_staff:
                return redirect('index_1_url')
            return redirect('index_url')
    return render(request, 'login.html')


def my_profile_view(request):
    return render(request, 'account.html')


def logout_view(request):
    logout(request)
    return redirect('login_url')
