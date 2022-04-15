from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('chapters.urls', 'chapters'), namespace='chapters')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('icons/python.ico'))),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
