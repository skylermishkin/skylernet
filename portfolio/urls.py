from django.urls import path

from . import views


app_name = 'portfolio'
urlpatterns = [
    path('', views.index, name='index'),
    path('project_test', views.project, name='project_test'),
    path('<string: project_name>', views.project),
]
