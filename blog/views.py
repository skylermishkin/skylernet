from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    num_posts_displayed = 3
    displayed_posts = Post.objects.order_by('-date_posted')[:num_posts_displayed]
    context = {'displayed_posts': displayed_posts}
    return render(request, 'blog/index.html', context)


def post(request, slug):
    post_obj = get_object_or_404(Post, slug=slug)
    context = {'post': post_obj}
    return render(request, 'blog/post.html', context)
