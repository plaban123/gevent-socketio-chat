from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

from socketio import sdjango
sdjango.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'geventsocketio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('echo_server.urls')),
    url(r'^socket\.io', include(sdjango.urls)),
)+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
