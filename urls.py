from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

from base import views as base_views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', base_views.Index.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
)
