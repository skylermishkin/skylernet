from django.shortcuts import render, get_object_or_404

from .models import Post, Tag


def get_displayed_posts(request):
    num_posts_displayed = 4
    if request.GET.get("num_posts"):
        num_posts_displayed = int(request.GET.get("num_posts"))
    if request.GET.get("tag"):
        return Post.objects.filter(tags__slug=request.GET.get("tag"))[:num_posts_displayed]
    return Post.objects.order_by('-date_posted')[:num_posts_displayed]


def index(request):
    displayed_posts = get_displayed_posts(request)
    tags = Tag.objects.all()
    context = {'displayed_posts': displayed_posts,
               'tags': tags}
    return render(request, 'blog/index.html', context)


def post(request, slug):
    post_obj = get_object_or_404(Post, slug=slug)
    context = {'post': post_obj}
    return render(request, 'blog/post.html', context)
