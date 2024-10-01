# View for blog
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import TrigramSimilarity

def index(request):
    # This view for home page
    return render(request, 'blog/index.html')


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
            result1 = Post.published.annotate(
                similarity=TrigramSimilarity('title', query)
            ).filter(similarity__gt=0.1)
            result2 = Post.published.annotate(
                similarity=TrigramSimilarity('description', query)
            ).filter(similarity__gt=0.1)
            results = (result1 | result2).order_by('-similarity')
    context = {
        'query': query,
        'results': results
    }
    return render(request, 'blog/search.html', context)

@login_required
def profile(request):
    # For show author posts
    user = request.user
    posts = Post.published.filter(author=user)
    return render(request, "blog/profile.html", {'posts': posts})

@login_required
def post_create(request):
    # For create new post
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            Image.objects.create(image_file=form.cleaned_data['image'], post=post)
            return redirect('blog:profile')
    else:
        form = CreatePostForm()
    return render(request, 'forms/create-post.html', {"form": form})

@login_required
def post_delete(request, pk):
    # For delete a post
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'پست مورد نظر حذف شد')
        return redirect('blog:profile')
    return render(request, 'forms/delete-post.html', {"post": post})

@login_required
def post_edit(request, pk):
    # For edit a post
    post = get_object_or_404(Post, id=pk)
    if request.method == 'POST':
        form = CreatePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            Image.objects.create(image_file=form.cleaned_data['image'], post=post)
            return redirect('blog:profile')
    else:
        form = CreatePostForm(instance=post)
    return render(request, 'forms/create-post.html', {"form": form, 'post': post})

@login_required
def image_delete(request, pk):
    # For delete post image when user edit a post
    image = get_object_or_404(Image, id=pk)
    image.delete()
    return redirect('blog:profile')

def register(request):
    # View for registration user
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'registration/register_done.html', {'user': user})
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
