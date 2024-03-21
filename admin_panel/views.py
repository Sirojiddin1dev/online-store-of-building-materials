from django.shortcuts import render, redirect
from main.models import Blog, Image, Tag, Category
from django.contrib.auth.decorators import login_required


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

