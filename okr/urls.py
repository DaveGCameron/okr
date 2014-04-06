from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'okr.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'okr.views.root', name='root'),
    url(r'^company/$', 'ork.views.company', name='company'),
    url(r'^kr/$', 'ork.views.kr', name='keyresult'),
    url(r'^admin/', include(admin.site.urls)),
)
