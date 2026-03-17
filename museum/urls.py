from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from . import views

admin.site.site_header = 'Музей трудовой и воинской славы'
admin.site.site_title = 'Администрирование музея'
admin.site.index_title = 'Управление контентом'

def preview_404(request):
    return render(request, '404.html', status=200)

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('fond/', include('apps.fond.urls', namespace='fond')),
    path('gallery/', include('apps.gallery.urls', namespace='gallery')),
    path('staff/', include('apps.staff.urls', namespace='staff')),
    path('map/', include('apps.mapblock.urls', namespace='mapblock')),
    path('news/', include('apps.news.urls', namespace='news')),
    path('admin/', admin.site.urls),
    path('404-preview/', preview_404),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
