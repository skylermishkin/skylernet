from django.shortcuts import render, get_object_or_404

from .models import Project


def index(request):
    num_projects_displayed = 4
    displayed_projects = Project.objects.order_by('-date_updated')[:num_projects_displayed]
    context = {'displayed_projects': displayed_projects}
    return render(request, 'portfolio/index.html', context)


def project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    context = {'project': project}
    return render(request, 'portfolio/project.html', context)
