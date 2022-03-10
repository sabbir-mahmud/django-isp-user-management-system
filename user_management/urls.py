# imports
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # home page and clients urls
    path('', include('apps.home.urls'), name='home-page'),
    # core devices urls
    path('inside/', include('apps.core.urls')),
    # accounts management urls
    path('account/', include('apps.account.urls')),
    # clients management urls
    path('clients/', include('apps.clients.urls')),
    # resellers management urls
    path('resellers/', include('apps.resellers.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
