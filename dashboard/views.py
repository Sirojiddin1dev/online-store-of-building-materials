from django.shortcuts import render
from .models import *
from main.admin import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse


def banner_view(request):
    basket = Basket.objects.filter(user_id=request.user.id)
    basket_count = Basket.objects.filter(user_id=request.user.id).count()
    subtotal = 0
    for item in basket:
        subtotal += item.product.price
    total = subtotal
    banner = Banner.objects.last()
    product1 = Future.objects.all().order_by('-id')[:2]
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
    try:
        product = Products.objects.get(pk=pk)
    except Products.DoesNotExist:
        return HttpResponse("Product does not exist")

    basket = Basket.objects.filter(user_id=request.user.id)
    basket_count = Basket.objects.filter(user_id=request.user.id).count()
    subtotal = 0
    for item in basket:
        subtotal += item.product.price
    total = subtotal
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


def PegenatorPage(List, num, request):
    paginator = Paginator(List, num)
    pages = request.GET.get('page')
    try:
        list = paginator.page(pages)
    except PageNotAnInteger:
        list = paginator.page(1)
    except EmptyPage:
        list = paginator.page(paginator.num_pages)
    return list


def all_products(request):
    product = Products.objects.all()
    context={
        'product': PegenatorPage(product, 10, request)
    }
    return render(request, 'apartment.html', context)


def all_info(request):
    info = Info.objects.last()
    context = {
        'info':info
    }
    return render(request, 'best_deals.html', context)


def all_checkout(request):
    checkout = Checkout.objects.all()
    context = {
        'checkout':PegenatorPage(checkout, 10, request)
    }
    return render(request, 'home_page.html',context)


def all_banner(request):
    banner = Banner.objects.last()
    context = {
        'banner':banner
    }
    return render(request, 'house.html', context)


def all_blog(request):
    blog = Blog.objects.all()
    context = {
        'blog': PegenatorPage(blog, 10, request)
    }
    return render(request,'popular_home.html', context)


def all_contact(request):
    contact = Contact.objects.all()
    context = {
        'contact': PegenatorPage(contact, 10, request)
    }
    return render(request,'villa.html', context)


