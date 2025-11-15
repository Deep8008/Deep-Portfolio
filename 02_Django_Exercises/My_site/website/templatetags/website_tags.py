from django import template
from blog.models import Post, Category

register = template.Library()

@register.inclusion_tag('website/website-latestposts.html')
def latestposts(count=6):
    filteredposts = Post.objects.filter(status = 1).order_by('-published_date')[:count]
    posts = {'posts': filteredposts}
    return posts
