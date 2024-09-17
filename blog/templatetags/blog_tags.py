# Template tags for blog app
from lib2to3.fixes.fix_input import context

from django import template
from ..models import Post, Comment

register = template.Library()


@register.simple_tag()
def total_posts():
    # a tag for total posts
    return Post.published.count()

@register.simple_tag()
def total_comments():
    # a tag for total comments
    return Comment.objects.filter(active=True).count()

@register.simple_tag()
def last_post():
    # a tag for last post date
    return Post.published.last().publish

@register.inclusion_tag("partials/latest_posts.html")
def latest_posts(count=4):
    l_posts = Post.published.order_by('-publish')[:count]
    context = {
        'l_posts': l_posts,
    }
    return context