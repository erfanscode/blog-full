# View for blog
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
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
