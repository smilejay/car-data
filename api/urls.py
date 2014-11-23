from django.conf.urls import patterns, url


urlpatterns = patterns('api.views',
    # Examples:
    # url(r'^$', 'car_data.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^demo_post/', 'demo_post'),
    url(r'^save_acceleration/', 'save_acceleration'),
    url(r'^save_loation/', 'save_loation'),
)