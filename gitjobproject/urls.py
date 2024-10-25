from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('gitjob.urls')), 
    path('users/', include('users.urls')),
    # path('jobs/', include('jobs.urls')),
    path("__reload__/", include("django_browser_reload.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)