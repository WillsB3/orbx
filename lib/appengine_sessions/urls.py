from django.conf.urls import *
from appengine_sessions import views

urlpatterns = patterns('',
    url(r'^clean-up/$', views.session_clean_up, name='session-clean-up'),
)
