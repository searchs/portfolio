from django.shortcuts import render, get_object_or_404
from .models import Blog


def allblogs(request):
    allblogs = Blog.objects
    return render(request, "blog/allblogs.html", {"allblogs": allblogs.all})


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, "blog/detail.html", {"detail": blog_detail})
