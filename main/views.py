from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from dashboard.models import *
from django.contrib.auth.decorators import login_required


def index_view(request):
    context = {
        'info': Info.objects.last()
    }
    return render(request, 'index.html', context)


def blog_view(request):
    context = {
        'blog': Blog.objects.all().order_by('-id')[:9],
        'info': Info.objects.last()
    }
    return render(request, 'blog.html', context)


def single_blog_view(request, pk):
    blog = Blog.objects.get(pk=pk)
    context = {
        'single_blog': blog,
        'blog': Blog.objects.all().order_by('-id')[:2],
        'category': Category.objects.all(),
        'tag': Tag.objects.all(),
        'info': Info.objects.last(),
        'recent_posts': Blog.objects.all().order_by('-id')[:4],
        'comment': Comment.objects.filter(blog=blog)
    }
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Comment.objects.create(
            name=name,
            message=message,
            blog=blog,
            email=email,
        )
        return redirect("single_blog_url", pk=blog.id)
    return render(request, 'blog-details.html', context)


def contact_view(request):
    context = {
        'info': Info.objects.last()
    }
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        message = request.POST['message']
        contact = Contact.objects.create(
            name=name,
            email=email,
            phone_number=phone_number,
            message=message,
        )
        return HttpResponse("Sizning so'rovingiz qabul qilindi! Sizga Tez orada Javob Berildi ")
    return render(request, 'contact.html', context)

@login_required
def remove_cart_product(request, pk):
    basket = Basket.objects.get(pk=pk)
    basket.delete()
    return HttpResponse("1 ta obyekt o'chirildi!")


def cart_view(request, id):
    basket = Basket.objects.filter(user_id=id)
    basket_count = Basket.objects.filter(user_id=id).count()
    subtotal = 0
    for item in basket:
        subtotal += item.product.price

    total = subtotal

    context = {
        'basket': basket,
        'basket_count': basket_count,
        'subtotal': subtotal,
        'total': total,
        'contact': Contact.objects.last(),
        'info': Info.objects.last()
    }
    return render(request, 'cart.html', context)


def checkout_view(request, pk):
    basket = Basket.objects.filter(user_id=pk)
    subtotal = 0
    for i in basket:
        subtotal += i.product.price
    total = subtotal
    context = {
        'basket': basket,
        'subtotal': subtotal,
        'total': total,
        'info': Info.objects.last()
    }
    products = ''
    for i in basket:
        products += f"Mahsulot nomi: {i.product.title}"
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST['address']
        country = request.POST['country']
        Checkout.objects.create(
            user_id=request.user.id,
            name=name,
            product=products,
            email=email,
            phone_number=phone_number,
            address=address,
            country=country,
        )
        return HttpResponse('<h1>Sizning Arizangiz qabul qilindi!</h1>')
    return render(request, 'checkout.html', context)


def add_basket(request, pk):
    product = Products.objects.get(pk=pk)
    Basket.objects.create(
        user=request.user,
        product=product,
    )
    return HttpResponse("Item added to basket successfully!")