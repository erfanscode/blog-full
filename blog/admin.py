from django.contrib import admin
from django_jalali.admin.filters import JDateFieldListFilter
# blog models
from .models import *

# Django admin panel Farsi
admin.sites.AdminSite.site_header = 'پنل مدیریت جنگو'
admin.sites.AdminSite.site_title = 'پنل'
admin.sites.AdminSite.index_title = 'مدیریت وبسایت'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'author', 'publish', 'status']
  list_filter = ['author', ('publish', JDateFieldListFilter), 'status']
  search_fields = ['title', 'description']
  list_editable = ['status']
  date_hierarchy = 'publish'
  raw_id_fields = ['author']
  prepopulated_fields = {'slug': ['title']}


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
  list_display = ['name', 'email', 'subject']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ['post', 'name', 'created', 'active']
  list_filter = ['active', ('created', JDateFieldListFilter), ('updated', JDateFieldListFilter)]
  search_fields = ['name', 'body']
  list_editable = ['active']
