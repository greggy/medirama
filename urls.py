from django.conf.urls.defaults import *
import settings

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^profile/', include('profile.urls')),

    # Uncomment this for admin:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
    (r'^static_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
        
)
