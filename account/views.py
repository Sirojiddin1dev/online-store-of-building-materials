from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login, logout, authenticate
from dashboard.models import Basket
from main.models import Info

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
    basket = Basket.objects.filter(user_id=id)
    basket_count = Basket.objects.filter(user_id=id).count()
    subtotal = 0
    for item in basket:
        subtotal += item.product.price
    total = subtotal
    user= User.objects.get(pk=pk)
    if request.method == "POST":
        username=request.POST['username']
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        bio=request.POST.get('bio')
        img=request.POST.get('img')
        login_count = request.POST.get('login_count')
        last_login = request.POST.get('last_login')
        phone_number=request.POST.get('phone_number')
        password=request.POST.get('password')
        confirm_password=request.POST.get('cofirm_password')
        user.username=username
        user.first_name=first_name
        user.last_name=last_name
        user.email =email
        user.bio=bio
        user.phone_number = phone_number
        if password is not None:
            if password == confirm_password:
                user.set_password(password)
        user.save()
        return redirect("my_profile_url", user.id)
    context = {
        'profile': request.user,
        'info': Info.objects.last(),
        'basket': basket,
        'basket_count': basket_count,
        'subtotal': subtotal,
        'total': total,
        'user': user
    }
    return render(request, 'account.html', context)


def logout_view(request):
    logout(request)
    return redirect('login_url')
