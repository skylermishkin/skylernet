from django.shortcuts import get_object_or_404, render


def index(request):
    context = {}
    return render(request, 'skylernet/landing.html', context)
