# Urls for Blog
from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.index, name="index"),
    path("create/", views.create_post, name="create_post"),
    path("preview/<pk>", views.pre_view, name="pre_view"),
    path("posts/", views.PostListView.as_view(), name="post_list"),
    path("posts/<pk>", views.post_detail, name="post_detail"),
    path("posts/<pk>/comment", views.post_comment, name="post_comment"),
    path("ticket", views.ticket, name="ticket"),
]
