from django.shortcuts import render, get_object_or_404


def index(request):
    context = {}
    return render(request, 'blog/index.html', context)


def post(request):
    context = {}
    return render(request, 'blog/post.html', context)
