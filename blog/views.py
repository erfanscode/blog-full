# View for blog
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.db.models import Q
from django.views.generic import ListView
from django.views.decorators.http import require_POST

def index(request):
    # This view for home page
    return render(request, 'blog/index.html')

def create_post(request):
    # view for create post
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.create = timezone.now()
            post.save()
            return redirect('blog:pre_view', post.pk)
    else:
        form = CreatePostForm()
    context = {
        'form': form,
    }
    return render(request, 'forms/create_post.html', context)



class PostListView(ListView):
    # class for post list
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 4
    template_name = 'blog/list.html'


def post_detail(request, pk):
    post = get_object_or_404(Post, id=pk, status=Post.Status.PUBLISHED)
    comments = post.comments.filter(active=True)
    form = CommentForm()
    context = {
        'post': post,
        'comments': comments,
        'form': form
    }
    return render(request, 'blog/detail.html', context)

# class PostDetailView(DetailView):
#     # class for post detail
#     model = Post
#     template_name = 'blog/detail.html'

def pre_view(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'blog/pre_view.html', {'post': post})

def ticket(request):
    # view for ticket form
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket_obj = Ticket.objects.create()
            cd = form.cleaned_data
            ticket_obj.message = cd['message']
            ticket_obj.name = cd['name']
            ticket_obj.email = cd['email']
            ticket_obj.phone = cd['phone']
            ticket_obj.subject = cd['subject']
            ticket_obj.save()
            return redirect('blog:ticket')
    else:
        form = TicketForm()
    return render(request, 'forms/ticket.html', {"form": form})

@require_POST
def post_comment(request, pk):
    # view for post comments
    post = get_object_or_404(Post, id=pk, status=Post.Status.PUBLISHED)
    comment = None
    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
    context = {
        'post': post,
        'form': form,
        'comment': comment
    }
    return render(request, 'forms/comment.html', context)

def post_search(request):
    # view for search posts
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(data=request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.published.filter(
                Q(title__icontains=query) | Q(description__icontains=query)
            )
    context = {
        'query': query,
        'results': results
    }
    return render(request, 'blog/search.html', context)
