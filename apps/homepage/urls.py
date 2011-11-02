from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('apps.homepage.views',
    # Examples:
    url(r'^$', 'index', name='homepage_home'),
    url(r'^about/$', 'about', name='homepage_about'),
    url(r'^archive/$', 'archive', name='homepage_archive'),
    url(r'^contact/$', 'contact', name='homepage_contact'),

)
