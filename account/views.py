from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login, logout, authenticate
from dashboard.models import Basket
from main.models import Info
from django.http import HttpResponse
from django.db import IntegrityError
from django.contrib import messages


def create_user_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')

        try:
            # Attempt to create the user
            user = User.objects.create_user(
                username=username,
                password=password,
                phone_number=phone_number,
                first_name = first_name,
                last_name = last_name,
            )
            return redirect('index_url')
        except IntegrityError:
            # Handle the case when the username is not unique
            error_message = "This username is already taken. Please choose a different one."
            messages.error(request, error_message)
            return render(request, 'login.html')

    return render(request, 'register.html')


def create_staff_user_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        is_staff = request.POST.get('is_staff', True) == 'on'
        if is_staff:
            is_staff = True
        try:
            User.objects.create_user(
                username=username,
                password=password,
                is_staff=is_staff,
            )
            return HttpResponse("Siz Staff User Qo'shdingiz ")
        except IntegrityError:
            return HttpResponse("This username is already taken. Please choose a different one.")
    return render(request, 'index_1.html')



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


def my_profile_view(request, pk):
    basket = Basket.objects.filter(user_id=request.user.id)
    basket_count = Basket.objects.filter(user_id=request.user.id).count()
    subtotal = 0
    for item in basket:
        subtotal += item.product.price
    total = subtotal
    context = {
        'info': Info.objects.last(),
        'basket': basket,
        'basket_count': basket_count,
        'subtotal': subtotal,
        'total': total,
        'user': request.user
    }
    return render(request, 'account.html', context)


def logout_view(request):
    logout(request)
    return redirect('login_url')
