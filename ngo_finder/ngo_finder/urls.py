from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ngo_finder.views.hello_world', name='home'),
    # url(r'^ngo_finder/', include('ngo_finder.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^ngolist', 'ngo_finder.views.ngolist'),
    url(r'^ngo/(\d+)', 'ngo_finder.views.ngo'),
)
