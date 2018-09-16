from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path, include

from . import views
from .settings_secret import ADMIN_URL_RESTRING


app_name = 'skylernet'

admin.site.site_header = 'SkylerNet Administration'
admin.site.site_title = 'SkylerNet Administration'

urlpatterns = [
    re_path(ADMIN_URL_RESTRING, admin.site.urls),
    path('', views.index, name='index'),
    path('blog/', include('blog.urls')),
    path('connect/', views.connect, name='connect'),
    path('portfolio/', include('portfolio.urls')),
]


# To access media files during development
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
