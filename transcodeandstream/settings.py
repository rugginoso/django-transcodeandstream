from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

TAS_WATCHED_DIRECTORIES = getattr(settings, 'TAS_WATCHED_DIRECTORIES', [])
if not TAS_WATCHED_DIRECTORIES:
	raise ImproperlyConfigured('No watched directories configured.')

TAS_VIDEOS_DIRECTORY = getattr(settings, 'TAS_VIDEOS_DIRECTORY', None)
if not TAS_VIDEOS_DIRECTORY:
	raise ImproperlyConfigured('No vidoes directory configured.')

TAS_VIDEO_EXTENSIONS = getattr(settings, 'TAS_VIDEO_EXTENSIONS', (
	'.avi',
	'.mov',
))