from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views


app_name = 'skylernet'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('blog/', include('blog.urls')),
    path('portfolio/', include('portfolio.urls')),
]


# So that I can access media files during development
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
