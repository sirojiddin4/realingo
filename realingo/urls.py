from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    
    # Django's built-in auth views
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Redirect any attempts to use the account/ URL pattern to the correct accounts/ path
    path('account/login/', RedirectView.as_view(url='/accounts/login/', permanent=True)),
    path('account/logout/', RedirectView.as_view(url='/accounts/logout/', permanent=True)),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)