from django.shortcuts import get_object_or_404, render
from django.contrib.staticfiles.templatetags.staticfiles import static


def index(request):
    return render(request, 'skylernet/landing.html')


def connect(request):
    context = {'online_media': [{"name": 'LinkedIn',
                                 'href': 'https://www.linkedin.com/in/skyler-mishkin-62446b158',
                                 'src': static('skylernet/LinkedIn.svg')},
                                {'name': 'GitHub',
                                 'href': 'https://github.com/skylermishkin',
                                 'src': static('skylernet/GitHub.png')}]}
    return render(request, 'skylernet/connect.html', context)
