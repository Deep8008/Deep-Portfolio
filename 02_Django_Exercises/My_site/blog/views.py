from django.shortcuts import render, get_object_or_404
from blog.models import Post
from django.utils import timezone

def blog_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status = 1)
    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)

def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid, status=1)

    prev_post = Post.objects.filter(id__lt=post.id).order_by('-id').first()
    next_post = Post.objects.filter(id__gt=post.id).order_by('id').first()

    context = {'posts': post, 'prev_post': prev_post, 'next_post': next_post}

    return render(request, "blog/blog-single.html", context)

def test(request, pid):
    posts = get_object_or_404(Post, pk=pid)
    context = {'posts': posts}
    return render(request, "test.html", context)
