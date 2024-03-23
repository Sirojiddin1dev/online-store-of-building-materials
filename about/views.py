from django.shortcuts import render
from .models import *


def about_view(request):
    about = About.objects.all().order_by('-id')[:1]
    context = {
        'about': about
    }
    return render(request, 'about.html', context)


