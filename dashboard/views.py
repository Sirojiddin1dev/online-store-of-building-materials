from django.shortcuts import render
from .models import *


def banner_view(request):
    banner = Products.objects.filter(is_banner=True).order_by('-id')[:2]
    product1 = Products.objects.filter(featured_product = True).order_by('-id')[:2]
    product2 = Products.objects.all().order_by('-view')[:4]
    product3 = Products.objects.filter(is_advert=True)[:3]
    product = Products.objects.filter(new_product=True).order_by('-id')[:12]
    context = {
        'banner': banner,
        "product1": product1,
        'product2': product2,
        'product3': product3,
        'product4': product4,
        'product5': product5,
    }
    return render(request, 'index.html', context)


def shopping_view(request):
    context={
        'shop': Products.objects.all().order_by('-id')[:7]
    }
    return render(request,'shop.html', context)
