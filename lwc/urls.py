from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'joins.views.home', name='home'),
    url(r'^about/$', 'joins.views.about', name='about'),
    url(r'^members/$', 'joins.views.members', name='members'),
    url(r'^contact/$', 'joins.views.contact', name='contact'),
    url(r'^methodology/$', 'joins.views.methodology', name='methodology'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
