from django.shortcuts import render
from .models import *


def banner_view(request):
    product = Products.objects.filter(is_banner=True).order_by('-id')[:2]
    context = {
        'banner': product
    }
    return render(request, 'product.html', context)


def product1_view(request):
    product = Products.objects.filter(featured_product = True).order_by('-id')[:2]
    context = {
        "product1": product
    }
    return render(request, 'product.html', context)


def product2_view(request):
    product = Products.objects.all().order_by('-view')[:4]
    context = {
        'product2': product
    }
    return render(request, 'product.html', context)


def product3_view(request):
    product = Products.objects.filter(is_advert = True)[:3]
    context = {
        'product3': product
    }
    return render(request, 'product.html', context)


def product4_view(request):
    product = Products.objects.all().order_by('-new_product')[:12]
    context = {
        'product4': product
    }
    return render(request, 'product.html', context)


def product5_view(request):
    product = Products.objects.all().order_by('-product_info')[:6]
    context = {
        'product5':product
    }
    return render(request, 'product.html', context)


def shopping_view(request):
    context={
        'shop': Products.objects.all().order_by('-id')[:7]
    }
    return render(request,'shop.html', context)
