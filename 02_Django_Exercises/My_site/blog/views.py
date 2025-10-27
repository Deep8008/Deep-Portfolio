from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from blog.models import Post
from django.utils import timezone

def blog_view(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status = 1)
    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)

def blog_single(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.counted_views += 1
    post.save(update_fields=['counted_views'])
    
    return render(request, "blog/blog-single.html")

def test(request, pid):
    posts = get_object_or_404(Post, pk=pid)
    context = {'posts': posts}
    return render(request, "test.html", context)
