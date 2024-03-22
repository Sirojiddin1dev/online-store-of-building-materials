from django.shortcuts import render
from .models import *

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