from django import template
from blog.models import Post, Category

register = template.Library()

@register.inclusion_tag('blog/blog-latest-posts.html')
def latestposts(count=1):
    filteredposts = Post.objects.filter(status = 1).order_by('-published_date')[:count]
    posts = {'posts': filteredposts}
    return posts

@register.inclusion_tag('blog/blog-category-widget.html')
def categories():
    categories = Category.objects.all()

    data = []

    for cat in categories:
        post_count = Post.objects.filter(status=1, category=cat).count()
        data.append({
            'name': cat.name,
            'count': post_count
        })

    result = {'categories': data}

    return result

@register.inclusion_tag('blog/blog-cloud-tags.html')
def cloud_tags():
    categories = Category.objects.all()

    data = []

    for cat in categories:
        post_count = Post.objects.filter(status=1, category=cat).count()
        data.append({
            'name': cat.name,
            'count': post_count
        })

    result = {'categories': data}

    return result
