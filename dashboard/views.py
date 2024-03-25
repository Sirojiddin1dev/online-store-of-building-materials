from django.shortcuts import render
from .models import *
from main.admin import *


def banner_view(request):
    banner = Banner.objects.last()
    product1 = Products.objects.filter(featured_product = True).order_by('-id')[:2]
    product2 = Products.objects.all().order_by('-view')[:4]
    product3 = Products.objects.filter(is_advert=True)[:3]
    product4 = Products.objects.filter(new_product=True).order_by('-id')[:12]
    blog = Blog.objects.all().order_by('-id')[:6]
    context = {
        'banner': banner,
        "product1": product1,
        'product2': product2,
        'product3': product3,
        'product4': product4,
        'blog': blog,
        'info': Info.objects.last(),
    }
    return render(request, 'index.html', context)


def shopping_view(request):
    context={
        'shop': Products.objects.all().order_by('-id')[:7]
    }
    return render(request,'shop.html', context)


def single_product(request, pk):
    product = Products.objects.get(pk=pk)
    product.view += 1
    product.save()
    context = {
        'product': product
    }
    return render(request, 'product.html', context)
