from django.shortcuts import render
from .models import *


def banner_view(request):
    product = Products.objects.filter(is_banner=True)
    context = {
        'product': Products.objects.all().order_by('-id')[:2]
    }
    return render(request, 'product.html', context)


def product_view(request):
    context ={
        "products":Products.objects.all().order_by('-id')[:2]
    }
    return render(request, 'product.html', context)


def product2_view(request):
    context={
        'products':Products.objects.all().order_by('-id')[:4]
    }
    return render(request, 'product.html', context)


def product3_view(request):
    context={
        'products':Products.objects.all().order_by('-id')[:2]
    }
    return render(request, 'product.html', context)