from django.contrib import admin
# blog models
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ['id', 'title', 'author', 'publish', 'status']
  list_filter = ['author', 'publish', 'status']
  search_fields = ['title', 'description', 'author']
  list_editable = ['status']
  date_hierarchy = 'publish'
  raw_id_fields = ['author']
  prepopulated_fields = {'slug': ['title']}
