from django.conf.urls import patterns, include, url

urlpatterns = patterns('transcodeandstream',
	url(r'^encoding-infos/$', 'views.encoding_infos', name='encoding-infos'),
	url(r'^manager/(?P<path>[A-Za-z0-9_\-/]+)?$', 'views.filesystem_operation', name='filesystem-operation'),
)
