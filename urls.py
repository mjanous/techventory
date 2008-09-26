from django.conf.urls.defaults import *
from django.conf import settings
from techventory.models import *

urlpatterns = patterns('techventory.views',
    url('^$',
        view='index',
        name='index',
    ),
    url(
        r'^servers/page(?P<page>[0-9]+)/$',
        view='server_list',
        name='server_list',
    ),
    url(
        r'^servers/(?P<object_id>\d+)/$',
        view='server_detail',
        name='server_detail',
    ),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (
            r'^site_media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}
        ),
    )