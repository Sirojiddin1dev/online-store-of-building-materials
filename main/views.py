from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse

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
        'recent_posts': Blog.objects.all().order_by('-id')[:4]
    }
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