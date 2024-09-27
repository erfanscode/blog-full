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
    path("profile/delete_post/<pk>", views.post_delete, name="post_delete"),
    path("profile/edit_post/<pk>", views.post_edit, name="post_edit"),
    path("profile/delete_image/<pk>", views.image_delete, name="image_delete"),
]
