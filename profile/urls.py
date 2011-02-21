from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'(?P<person_id>\d+)/$', 'profile.views.get_profile', name='get-profile'),
    url(r'add/$', 'profile.views.add_profile', name='add-profile'),
)
