from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index_view(request):
    context = {
        'info': Info.objects.last()
    }
    return render(request, 'index.html', context)


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


def blog_view(request):
    blog = Blog.objects.all()
    context = {
        'a': PegenatorPage(blog, 9, request),
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