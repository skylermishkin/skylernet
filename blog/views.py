from django.shortcuts import render

from .models import Post


def index(request):
    num_posts_displayed = 3
    displayed_posts = Post.objects.order_by('-date_posted')[:num_posts_displayed]
    context = {'displayed_posts': displayed_posts}
    return render(request, 'blog/index.html', context)


def post(request):
    context = {}
    return render(request, 'blog/post.html', context)
