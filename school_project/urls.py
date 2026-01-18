from django.contrib import admin
from django.urls import path, include
# Import these two lines to handle static/media files
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("presentation.urls")),
]

# This is the standard and correct way to serve user-uploaded media files
# (like your facility images) in a development environment.
if settings.DEBUG:
    # This line tells Django: when a request comes in for a URL starting
    # with settings.MEDIA_URL (i.e., '/media/'), find the corresponding
    # file inside the settings.MEDIA_ROOT directory (the 'media' folder).
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)