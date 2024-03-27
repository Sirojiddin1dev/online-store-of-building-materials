from django.shortcuts import render, redirect
from main.models import *
from django.contrib.auth.decorators import login_required
from dashboard.models import *
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseBadRequest
from account.models import *



def index_1_view(request):
    user = User.objects.filter(is_staff=True).order_by('-id')[:8]
    total_login_count = User.get_total_login_count()
    print(total_login_count)
    context = {
        'user':user,
        'count': total_login_count
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
        featured_product = request.POST.get('featured_product', False) == 'on'
        is_advert = request.POST.get('is_advert', False) == 'on'
        advert_text = request.POST.get('advert_text')
        advert_text_uz = request.POST.get('advert_text_uz')
        advert_text_ru = request.POST.get('advert_text_ru')
        advert_text_en = request.POST.get('advert_text_en')
        new_product = request.POST.get('new_product', True) == 'on'

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
    return render(request, 'index_1.html')

def update_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
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
        featured_product = request.POST.get('featured_product', False) == 'on'
        is_advert = request.POST.get('is_advert', False) == 'on'
        advert_text = request.POST.get('advert_text')
        advert_text_uz = request.POST.get('advert_text_uz')
        advert_text_ru = request.POST.get('advert_text_ru')
        advert_text_en = request.POST.get('advert_text_en')
        new_product = request.POST.get('new_product', True) == 'on'

        # Update the product object with the new data
        product.image = image
        product.title = title
        product.title_uz = title_uz
        product.title_ru = title_ru
        product.title_en = title_en
        product.price = price
        product.product_info = product_info
        product.product_info_uz = product_info_uz
        product.product_info_ru = product_info_ru
        product.product_info_en = product_info_en
        product.category = category
        product.quantity = quantity
        product.featured_product = featured_product
        product.is_advert = is_advert
        product.advert_text = advert_text
        product.advert_text_uz = advert_text_uz
        product.advert_text_ru = advert_text_ru
        product.advert_text_en = advert_text_en
        product.new_product = new_product

        # Save the updated product
        product.save()

        return redirect('single_product_url', pk=product.pk)  # Redirect to the detail view of the updated product
    return render(request, 'apartment.html', {'product': product})


def delete_product(request, pk):
    product = get_object_or_404(Products, pk=pk)
    product.delete()
    return redirect('all_products_url')


def info_create(request):
    if request.method == 'POST':
        logo = request.FILES.get('logo')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        facebook = request.POST.get('facebook')
        youtube = request.POST.get('youtube')
        twitter = request.POST.get('twitter')

        Info.objects.create(
            logo=logo,
            address=address,
            email=email,
            phone_number=phone_number,
            facebook=facebook,
            youtube=youtube,
            twitter=twitter
        )
        return redirect('all_info_url')  # Redirect to the detail view of the created Info object
    return render(request, 'index_1-.html')


def info_update(request, pk):
    info = get_object_or_404(Info, pk=pk)
    if request.method == 'POST':
        info.logo = request.FILES.get('logo', info.logo)
        info.address = request.POST.get('address', info.address)
        info.email = request.POST.get('email', info.email)
        info.phone_number = request.POST.get('phone_number', info.phone_number)
        info.facebook = request.POST.get('facebook', info.facebook)
        info.youtube = request.POST.get('youtube', info.youtube)
        info.twitter = request.POST.get('twitter', info.twitter)
        info.save()
        return redirect('all_info_url')
    return render(request, 'best-deals.html', {'info': info})


def info_delete(request, pk):
    info = get_object_or_404(Info, pk=pk)
    info.delete()
    return redirect('all_info_url')  # Redirect to a list view after deletion


def create_banner(request):
    if request.method == 'POST':
        title = request.POST['title']
        title_uz = request.POST['title_uz']
        title_ru = request.POST['title_ru']
        title_en = request.POST['title_en']
        img = request.FILES['img']
        Banner.objects.create(
            title=title,
            title_uz=title_uz,
            title_ru=title_ru,
            title_en=title_en,
            img=img
        )
        return redirect('all_banner_url')  # Redirect to a URL that lists all banners
    return render(request, 'index_1.html')


def update_banner(request, pk):
    banner = Banner.objects.get(pk=pk)
    if request.method == 'POST':
        banner.title = request.POST['title']
        banner.title_uz = request.POST['title_uz']
        banner.title_ru = request.POST['title_ru']
        banner.title_en = request.POST['title_en']
        if 'img' in request.FILES:
            banner.img = request.FILES['img']
        banner.save()
        return redirect('all_banner_url')
    return render(request, 'house.html', {'banner': banner})


def delete_banner(request, pk):
    banner = Banner.objects.get(pk=pk)
    banner.delete()
    return redirect('house.html')


def create_blog(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST['title']
        title_uz = request.POST['title_uz']
        title_ru = request.POST['title_ru']
        title_en = request.POST['title_en']
        description = request.POST['description']
        description_uz = request.POST['description_uz']
        description_ru = request.POST['description_ru']
        description_en = request.POST['description_en']
        category = request.POST['category']
        image = request.FILES.get('image')
        tags = request.POST['tags']  # List of tag IDs
        Blog.objects.create(
            user=user,
            title=title,
            title_uz=title_uz,
            title_ru=title_ru,
            title_en=title_en,
            description=description,
            description_uz=description_uz,
            description_ru=description_ru,
            description_en=description_en,
            category=category,
            image=image,
            tags=tags
        )
        return redirect('all_blog_url')

    return render(request, 'popular_home.html',)


def update_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.title_uz = request.POST.get('title_uz')
        blog.title_ru = request.POST.get('title_ru')
        blog.title_en = request.POST.get('title_en')
        blog.image = request.FILES.get('image')
        blog.description = request.POST.get('description')
        blog.description_uz = request.POST.get('description_uz')
        blog.description_ru = request.POST.get('description_ru')
        blog.description_en = request.POST.get('description_en')
        blog.category = request.POST.get('category')
        blog.tags = request.POST.get('tags')
        blog.save()
        return redirect('all_blog_url')  # Assuming you have a URL named 'blog_detail' for viewing blog details
    return render(request, 'popular_home.html',)


def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    blog.delete()
    return redirect('all_blog_url')  # Assuming you have a URL named 'blog_list' for listing blogs


def delete_checkout(request, pk):
    blog = get_object_or_404(Checkout, pk=pk)
    blog.delete()
    return redirect('all_checkout_url')
