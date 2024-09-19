# Template tags for blog app
from django import template
from django.db.models import Count, Max, Min
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

@register.simple_tag()
def most_popular_posts(count=4):
    # a tag for showing most popular posts using comment number
    return Post.published.annotate(
        comments_count=Count('comments')
    ).order_by('-comments_count')[:count]

@register.inclusion_tag("partials/latest_posts.html")
def latest_posts(count=4):
    l_posts = Post.published.order_by('-publish')[:count]
    context = {
        'l_posts': l_posts,
    }
    return context

@register.simple_tag()
def get_extreme_reading_time_posts():
    # give max and min reading posts
    result = Post.published.aggregate(
        max_time=Max('reading_time'),
        min_time=Min('reading_time')
    )
    max_post = Post.published.filter(reading_time=result['max_time']).first()
    min_post = Post.published.filter(reading_time=result['min_time']).first()
    context = {
        'max_post': max_post,
        'min_post': min_post,
    }
    return context
