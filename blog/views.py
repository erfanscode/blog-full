# View for blog
from django.http import HttpResponse

def index(request):
    return HttpResponse("Home Page")

def post_list(request):
    return HttpResponse("Posts")

def post_detail(request, id):
    return HttpResponse(f"Post: {id}")
