from django.shortcuts import render, get_object_or_404
from blog.models import Post, Comment
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import CommentForm
from django.contrib import messages


def blog_view(request, **kwargs):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status = 1)
    
    if kwargs.get('cat_name') != None :
        posts = posts.filter(category__name=kwargs.get('cat_name'))

    if kwargs.get('username') != None :
        posts = posts.filter(author__username=kwargs.get('username'))

    if kwargs.get('tag_name') != None :
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    posts = Paginator(posts, 3)

    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)

    except PageNotAnInteger:
        posts = posts.get_page(1)
    
    except EmptyPage:
        posts = posts.get_page(1)
        
    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)


def blog_single(request, pid):
    posts = get_object_or_404(Post, pk=pid, status=1)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = posts 
            form.save()
            messages.success(request, "Your Comment submited Succsessfuly!")
        else:
            messages.error(request, "Your Comment didnt submit!")

    prev_post = Post.objects.filter(id__lt=posts.id).order_by('-id').first()
    next_post = Post.objects.filter(id__gt=posts.id).order_by('id').first()

    comments = Comment.objects.filter(post=posts.id, approved=True)
    form = CommentForm()

    context = {'posts': posts, 'comments': comments, 'form': form, 'prev_post': prev_post, 'next_post': next_post}
    return render(request, "blog/blog-single.html", context)


def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context)

def blog_search(request):
    posts = Post.objects.filter(published_date__lte=timezone.now(), status = 1)

    if request.method == 'GET':
        if srch := request.GET.get('s'):
            posts = posts.filter(content__contains=srch)
    
    context = {'posts': posts}
    return render(request, "blog/blog-home.html",context)
