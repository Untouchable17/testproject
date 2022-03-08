from django.shortcuts import render
from .models import Blog


def index(request):

    blogs = Blog.objects.all()

    context = {
        'blogs': blogs
    }
    return render(request, "accounts/index.html", context)
