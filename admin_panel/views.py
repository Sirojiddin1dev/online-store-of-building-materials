from django.shortcuts import render


def index_1_view(request):
    return render(request, 'index_1.html')
