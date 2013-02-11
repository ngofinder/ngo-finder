from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'directory.views.main', name='home'),
    url(r'^login/', 'auth.views.login_user'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    #url(r'^ngolist', 'directory.views.ngolist'),
    url(r'^ngo/(\d+)', 'directory.views.ngo'),
    url(r'^contact/', 'directory.views.contact'),
    url(r'^about/', 'directory.views.about'),

    # search routes
    (r'^search/', include('haystack.urls')),
)
