# View for blog
from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post

def index(request):
    # This view for home page
    return HttpResponse("Home Page")

def post_list(request):
    # This view for showing all posts
    posts = Post.published.all()
    context = {
        'posts': posts
    }
    return render(request, "blog/list.html", context)

def post_detail(request, id):
    # This view for showing detail post
    try:
        post = Post.published.get(id=id)
    except:
        raise Http404("Post Not Found")
    context = {
        'post': post
    }
    return render(request, "blog/detail.html", context)
