# Urls for Blog
from django.urls import path
from . import views
from django.contrib.auth import views as auth_view

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
    path("login/", auth_view.LoginView.as_view(), name="login"),
    path("logout/", auth_view.LogoutView.as_view(), name="logout"),
    path("password-change/", auth_view.PasswordChangeView.as_view(success_url='done'), name="password_change"),
    path("password-change/done", auth_view.PasswordChangeDoneView.as_view(), name="password_change_done"),
]
