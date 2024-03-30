from django.contrib import admin
from django.urls import path, include
from LIB import settings
from django.conf.urls.static import static

# main routs
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.book.urls')),
    path('', include('apps.user.urls')),
]

# additional routs
if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include('debug_toolbar.urls')),
    ]+urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
