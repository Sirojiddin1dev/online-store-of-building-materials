from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login, logout, authenticate
from dashboard.models import Basket
from main.models import Info
from django.http import HttpResponse


def create_user_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        User.objects.create_user(
            username=username,
            password=password,
            phone_number=phone_number,
            email=email
        )
        return redirect('login_url')
    return render(request, 'register.html')


def create_staff_user_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        is_staff = request.POST.get('is_staff', 'false') == 'true'
        print(is_staff)
        user = User.objects.create_user(
            username=username,
            password=password,
            is_staff=is_staff,
        )
        user.save()
        return HttpResponse("Sizning so'rovingiz qabul qilindi! Sizga Tez orada Javob Berildi ")
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
