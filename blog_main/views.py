from django.shortcuts import render, redirect
from blogs.models import Category, Blog
def home(request):
    categories = Category.objects.all()
    featured_post = Blog.objects.filter(is_featured=True)

    context = {
        'categories': categories,
        'featured_post': featured_post,
        }

    return render(request, 'index.html', context)