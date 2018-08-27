from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'portfolio/index.html', context)


def project(request):
    context = {}
    return render(request, 'portfolio/project.html', context)

