from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'raxui.views.index', name='index'),
    url(r'^dashboard/', 'raxui.views.dashboard', name='dashboard'),

    url(r'^admin/', include(admin.site.urls)),
)
