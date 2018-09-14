from django.shortcuts import get_object_or_404, render


def index(request):
    return render(request, 'skylernet/landing.html')


def connect(request):
    context = {'social_media': []}
    return render(request, 'skylernet/connect.html', context)
