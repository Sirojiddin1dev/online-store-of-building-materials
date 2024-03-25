from django.shortcuts import render, redirect
from main.models import *
from django.contrib.auth.decorators import login_required
from dashboard.models import *
from .forms import *


def index_1_view(request):
    user = User.objects.filter(is_staff=True).order_by('-id')[:8]
    context = {
        'user':user
    }
    return render(request, 'index_1.html', context)


@login_required
def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # or any other URL you want to redirect after saving
    else:
        form = BlogForm()
    return render(request, 'create_blog.html', {'form': form})


def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Success URLni o'rnating
    else:
        form = ProductForm()
    return render(request, 'create_product.html', {'form': form})


def create_info(request):
    if request.method == 'POST':
        form = InfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Success url-ni o'zgartiring
    else:
        form = InfoForm()
    return render(request, 'info_form.html', {'form': form})


def create_banner(request):
    if request.method == 'POST':
        form = BannerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success_url')  # Redirect to a success URL after form submission
    else:
        form = BannerForm()
    return render(request, 'create_banner.html', {'form': form})