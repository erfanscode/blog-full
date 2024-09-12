from django.contrib import admin
# blog models
from .models import Post

# Django admin panel Farsi
admin.sites.AdminSite.site_header = 'پنل مدیریت جنگو'
admin.sites.AdminSite.site_title = 'پنل'
admin.sites.AdminSite.index_title = 'مدیریت وبسایت'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'author', 'publish', 'status']
  list_filter = ['author', 'publish', 'status']
  search_fields = ['title', 'description']
  list_editable = ['status']
  date_hierarchy = 'publish'
  raw_id_fields = ['author']
  prepopulated_fields = {'slug': ['title']}
