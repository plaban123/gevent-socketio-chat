from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from socketio import sdjango
sdjango.autodiscover()

urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + patterns('',
    # Examples:
    # url(r'^$', 'geventsocketio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('chat.urls')),
)
