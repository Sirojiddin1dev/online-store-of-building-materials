from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login, logout, authenticate
from dashboard.models import Ad


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
    return render(request, 'reg.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        usr = authenticate(username=username, password=password)
        if usr is not None:
            login(request, usr)
            return redirect('index_url')
    return render(request, 'login.html')


def my_profile_view(request):
    user = request.user
    count = Ad.objects.filter(user=user).order_by('id').count
    ad = Ad.objects.filter(user=user).order_by('-id')[:8]
    context = {
        'user': request.user,
        'count': count,
        'ad': ad,
    }
    return render(request, 'profile.html', context)


def logout_view(request):
    logout(request)
    return redirect('login_url')
