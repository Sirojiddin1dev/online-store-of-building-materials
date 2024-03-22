from django.shortcuts import render
from .models import *


def product_view(request):
    product = Products.objects.filter(is_banner=True)
    context = {
        'banner': Products.objects.all().order_by('-id')[:2],
        "product1": Products.objects.all().order_by('-id')[:2],
        'product2': Products.objects.all().order_by('-id')[:4],
        'product3': Products.objects.all().order_by('-id')[:3],
        'product4': Products.objects.all().order_by('-id')[:12],
        'product5': Products.objects.all().order_by('-id')[:3],
    }
    return render(request, 'product.html', context)



def shopping_view(request):
    context={
        'shop': Products.objects.all().order_by('-id')[:6]
    }
    return render(request,'shop.html', context)
