from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects
    return render(request, 'blogs/all_blogs.html', {'blogs': blogs})


def detailed_blog(request, blog_id):
    detailed = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogs/detailed.html', {'detailed': detailed})
