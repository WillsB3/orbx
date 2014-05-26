from django.conf.urls import *

urlpatterns = patterns(
    '',
    (r'^appengine_sessions/', include('appengine_sessions.urls')),
    (r'', include('core.urls')),
)
