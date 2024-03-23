from django.shortcuts import render
from .models import *


def about_view(request):
    about = About.objects.last()
    context = {
        'about': about
    }
    return render(request, 'about.html', context)


