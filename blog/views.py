# View for blog
from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView, DetailView

def index(request):
    # This view for home page
    return HttpResponse("Home Page")

class PostListView(ListView):
    # class for post list
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 4
    template_name = 'blog/list.html'


class PostDetailView(DetailView):
    # class for post detail
    model = Post
    template_name = 'blog/detail.html'
