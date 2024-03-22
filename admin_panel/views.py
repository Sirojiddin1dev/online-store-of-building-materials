from django.shortcuts import render, redirect
from main.models import Blog, Image, Tag, Category
from django.contrib.auth.decorators import login_required
from dashboard.models import *


def index_1_view(request):
    return render(request, 'index_1.html')


@login_required
def create_blog(request):
    if request.method == "POST":
        user = request.user
        title = request.POST.get('title')
        description = request.POST.get('description')
        category_id = request.POST.get('category')
        category = Category.objects.get(id=category_id)
        tags = request.POST.getlist('tags')
        images = request.FILES.getlist('images')

        # Create the blog instance
        blog = Blog.objects.create(user=user, title=title, description=description, category=category)

        # Add tags to the blog
        for tag_id in tags:
            tag = Tag.objects.get(id=tag_id)
            blog.tags.add(tag)

        # Add images to the blog
        for image in images:
            img = Image.objects.create(img=image)
            blog.img.add(img)

        return redirect('blog_detail')  # Redirect to the detail view of the created blog

    categories = Category.objects.all()
    tags = Tag.objects.all()
    return render(request, 'create_blog.html', {'categories': categories, 'tags': tags})



def create_product(request):
    if request.method == "POST":
        image = request.FILES.get('image')
        title_uz = request.POST.get('title_uz')
        title_ru = request.POST.get('title_ru')
        title_en = request.POST.get('title_en')
        price = request.POST.get('price')
        product_info_uz = request.POST.get('product_info_uz')
        product_info_ru = request.POST.get('product_info_ru')
        product_info_en = request.POST.get('product_info_en')
        category = request.POST.get('category')
        is_banner = request.POST.get('is_banner') == 'on'
        banner_title = request.POST.get('banner_title')
        banner_text = request.POST.get('banner_text')
        shop_collections = request.POST.get('shop_collections') == 'on'
        featured_product = request.POST.get('featured_product') == 'on'
        is_advert = request.POST.get('is_advert') == 'on'
        advert_text = request.POST.get('advert_text')
        new_product = request.POST.get('new_product') == 'on'

        # Create product instances for each language
        product_uz = Products.objects.create(
            image=image, title=title_uz, price=price, product_info=product_info_uz,
            category=category, is_banner=is_banner, banner_title=banner_title,
            banner_text=banner_text, shop_collections=shop_collections,
            featured_product=featured_product, is_advert=is_advert,
            advert_text=advert_text, new_product=new_product
        )
        product_ru = Products.objects.create(
            image=image, title=title_ru, price=price, product_info=product_info_ru,
            category=category, is_banner=is_banner, banner_title=banner_title,
            banner_text=banner_text, shop_collections=shop_collections,
            featured_product=featured_product, is_advert=is_advert,
            advert_text=advert_text, new_product=new_product
        )
        product_en = Products.objects.create(
            image=image, title=title_en, price=price, product_info=product_info_en,
            category=category, is_banner=is_banner, banner_title=banner_title,
            banner_text=banner_text, shop_collections=shop_collections,
            featured_product=featured_product, is_advert=is_advert,
            advert_text=advert_text, new_product=new_product
        )

        return redirect('product_detail', pk=product_uz.pk)  # Redirect to product detail view (choose one language)

    return render(request, 'create_product.html')
