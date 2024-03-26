from django.shortcuts import render, redirect
from main.models import *
from django.contrib.auth.decorators import login_required
from dashboard.models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest



def index_1_view(request):
    user = User.objects.filter(is_staff=True).order_by('-id')[:8]
    context = {
        'user':user
    }
    return render(request, 'index_1.html', context)


def create_product(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        title = request.POST.get('title')
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        title_en = request.POST.get('title_en')
        price = request.POST.get('price')
        product_info = request.POST.get('product_info')
        product_info_uz = request.POST.get('product_info_uz')
        product_info_ru = request.POST.get('product_info_ru')
        product_info_en = request.POST.get('product_info_en')
        category = request.POST.get('category')
        quantity = request.POST.get('quantity')
        featured_product = request.POST.get('featured_product', False)
        is_advert = request.POST.get('is_advert', False)
        advert_text = request.POST.get('advert_text')
        advert_text_uz = request.POST.get('advert_text_uz')
        advert_text_ru = request.POST.get('advert_text_ru')
        advert_text_en = request.POST.get('advert_text_en')
        new_product = request.POST.get('new_product', True)

        product = Products.objects.create(
            image=image,
            title=title,
            title_uz=title_uz,
            title_ru=title_ru,
            title_en=title_en,
            price=price,
            product_info=product_info,
            product_info_uz=product_info_uz,
            product_info_ru=product_info_ru,
            product_info_en=product_info_en,
            category=category,
            quantity=quantity,
            featured_product=featured_product,
            is_advert=is_advert,
            advert_text=advert_text,
            advert_text_uz=advert_text_uz,
            advert_text_ru=advert_text_ru,
            advert_text_en=advert_text_en,
            new_product=new_product
        )
        return redirect('single_product_url', pk=product.pk)  # Redirect to the detail view of the created product
    return render(request, 'index.html')

def update_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        # Update the product with the new data from the form
        product.image = request.FILES.get('image')
        product.title = request.POST.get('title')
        product.price = request.POST.get('price')
        product.product_info = request.POST.get('product_info')
        product.category = request.POST.get('category')
        product.quantity = request.POST.get('quantity')
        product.is_banner = request.POST.get('is_banner', False)
        product.banner_title = request.POST.get('banner_title')
        product.banner_text = request.POST.get('banner_text')
        product.shop_collections = request.POST.get('shop_collections', False)
        product.featured_product = request.POST.get('featured_product', False)
        product.is_advert = request.POST.get('is_advert', False)
        product.advert_text = request.POST.get('advert_text')
        product.new_product = request.POST.get('new_product', True)
        product.save()
        return redirect('product_detail', pk=pk)  # Redirect to the detail view of the updated product
    return render(request, 'update_product.html', {'product': product})

def delete_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')  # Redirect to the list view of products after deletion
    return HttpResponseBadRequest("Invalid request method")