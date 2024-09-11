# View for blog
from lib2to3.fixes.fix_input import context

from django.shortcuts import render
from django.http import HttpResponse
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
    render(request, "template.html", context)

def post_detail(request, id):
    # This view for showing detail post
    post = Post.published.get(id=id)
    context = {
        'post': post
    }
    render(request, "template2.html", context)
