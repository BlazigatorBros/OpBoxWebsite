from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OpBoxWebsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^scripts/', views.scripts, name='scripts'),
    url(r'^logs/(?P<title>[\w.]{0,256})', views.logs, name='logs'),
    url(r'^run/(?P<title>[\w.]{0,256})', views.run, name='run'),
    url(r'^rm/(?P<title>[\w.]{0,256})', views.rm, name='rm'),
    url(r'^edit/(?P<title>[\w.]{0,256})', views.edit, name='edit'),
    url(r'^write/(?P<title>[\w.]{0,256})', views.write, name='write'),
    url(r'^controller/(?P<title>[\w.]{0,256})', views.controller, name='controller'),
    url(r'^$', views.home, name='home')

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
