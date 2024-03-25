from django.shortcuts import render
from .models import *
from main.admin import *


def banner_view(request):
    basket = Basket.objects.filter(user_id=request.user.id)
    basket_count = Basket.objects.filter(user_id=request.user.id).count()
    subtotal = 0
    for item in basket:
        subtotal += item.product.price
    total = subtotal
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
        'basket': basket,
        'basket_count': basket_count,
        'subtotal': subtotal,
        'total': total,
    }
    return render(request, 'index.html', context)


def shopping_view(request):
    basket = Basket.objects.filter(user_id=request.user.id)
    basket_count = Basket.objects.filter(user_id=request.user.id).count()
    subtotal = 0
    for item in basket:
        subtotal += item.product.price
    total = subtotal
    context={
        'shop': Products.objects.all().order_by('-id')[:10],
        'info': Info.objects.last(),
        'basket': basket,
        'basket_count': basket_count,
        'subtotal': subtotal,
        'total': total,
    }
    return render(request,'shop.html', context)


def single_product(request, pk):
    basket = Basket.objects.filter(user_id=request.user.id)
    basket_count = Basket.objects.filter(user_id=request.user.id).count()
    subtotal = 0
    for item in basket:
        subtotal += item.product.price
    total = subtotal
    product = Products.objects.get(pk=pk)
    product2 = Products.objects.all().order_by('-view')[:4]
    product.view += 1
    product.save()
    context = {
        'product': product,
        'product2': product2,
        'info': Info.objects.last(),
        'basket': basket,
        'basket_count': basket_count,
        'subtotal': subtotal,
        'total': total,
    }
    return render(request, 'product.html', context)
