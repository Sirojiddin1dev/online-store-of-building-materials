from django.shortcuts import render
from .models import *
from dashboard.models import Basket
from main.models import Info


def about_view(request):
    basket = Basket.objects.filter(user_id=request.user.id)
    basket_count = Basket.objects.filter(user_id=request.user.id).count()
    subtotal = 0
    for item in basket:
        subtotal += item.product.price
    total = subtotal
    about = About.objects.last()
    context = {
        'about': about,
        'info': Info.objects.last(),
        'basket': basket,
        'basket_count': basket_count,
        'subtotal': subtotal,
        'total': total,
    }
    return render(request, 'about.html', context)


