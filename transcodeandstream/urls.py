from django.conf.urls import patterns, include, url

urlpatterns = patterns('transcodeandstream',
                       url(r'^$',
                           'views.filesystem_operation', name='manager'),

                       url(r'^manager/(?P<path>[A-Za-z0-9_\-\./\s]+)?$',
                           'views.filesystem_operation', name='filesystem-operation'),

                       url(r'^queue/$',
                           'views.queue', name='queue'),

                       url(r'^queue/(?P<video_id>[A-Za-z0-9_\-]{10})/log/$',
                           'views.queue_log', name='queue-log'),

                       url(r'^queue-data/$',
                           'views.queue_data', name='queue-data'),
                       )
