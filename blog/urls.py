# Urls for Blog
from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("", views.index, name="index"),
    path("posts/", views.PostListView.as_view(), name="post_list"),
    path("posts/<pk>", views.post_detail, name="post_detail"),
    path("posts/<pk>/comment", views.post_comment, name="post_comment"),
    path("ticket", views.ticket, name="ticket"),
    path("search/", views.post_search, name="post_search"),
    path("profile/", views.profile, name="profile"),
    path("profile/create_post", views.post_create, name="post_create"),
]
