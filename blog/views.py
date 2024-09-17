# View for blog
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.views.generic import ListView
from django.views.decorators.http import require_POST

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
    form = CommentForm(request.POST)
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
