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


TAS_FFMPEG_EXECUTABLE = getattr(
    settings,
    'TAS_FFMPEG_EXECUTABLE',
    '/usr/bin/ffmpeg')

TAS_FFMPEG_OPTIONS = getattr(
    settings,
    'TAS_FFMPEG_OPTIONS',
    []
)

TAS_FFMPEG_FORMATS_OPTIONS = getattr(
    settings,
    'TAS_FFMPEG_FORMATS_OPTIONS',
    {
        'webm': ['-vcodec', 'libvpx', '-acodec', 'libvorbis'],
        'mp4': [],
        'ogg': [],
    }
)

TAS_TRANSCODER_POLL_SECONDS = getattr(
    settings,
    'TAS_TRANSCODER_POLL_SECONDS',
    10)

TAS_DELETE_AFTER_TRANSCODE = getattr(settings, 'TAS_DELETE_AFTER_TRANSCODE', True)

TAS_TRANSCODER_FORMATS = getattr(
    settings,
    'TAS_TRANSCODER_FORMATS',
    ('webm',)
)
