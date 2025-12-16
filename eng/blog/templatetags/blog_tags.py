from django import template
from blog.models import Post

register = template.Library()

@register.inclusion_tag('blog/snippets/latest_posts.html')
def show_latest_posts(count=3):
    latest_posts = Post.objects.filter(published=True).order_by('-created_at')[:count]
    return {'latest_posts': latest_posts}