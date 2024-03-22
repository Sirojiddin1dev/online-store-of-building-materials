from django.shortcuts import render
from .models import *


def product_view(request):
    product = Products.objects.filter(is_banner=True)
    context = {
        'banner': Products.objects.all().order_by('-id')[:2],
    }
    return render(request, 'product.html', context)


def product1_view1(request):
    context = {
        "product1": Products.objects.all().order_by('-id')[:2],
    }
    return render(request, 'product.html', context)


def product2_view(request):
    context = {
        'product2': Products.objects.all().order_by('-id')[:4],
    }
    return render(request, 'product.html', context)


def product3_view(request):
    context = {
        'product3': Products.objects.all().order_by('-id')[:3],
    }
    return render(request, 'product.html', context)


def product4_view(request):
    context = {
        'product4': Products.objects.all().order_by('-id')[:12],
    }
    return render(request, 'product.html', context)


def product5_view(request):
    context = {
        'product5': Products.objects.all().order_by('-id')[:3],
    }
    return render(request, 'product.html', context)


def shopping_view(request):
    context={
        'shop': Products.objects.all().order_by('-id')[:6]
    }
    return render(request,'shop.html', context)
