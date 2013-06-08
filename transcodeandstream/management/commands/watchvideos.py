from django.core.management.base import BaseCommand, CommandError
from optparse import make_option

from transcodeandstream.models import EncodeQueueEntry
from transcodeandstream.settings import TAS_WATCHED_DIRECTORIES, TAS_VIDEO_EXTENSIONS

from _watcher import watch
from _random import generate_random_unique_name


def add_entry(path):
    existing_names = [entry['id'] for entry in EncodeQueueEntry.objects.values('id')]
    name = generate_random_unique_name(existing_names)
    entry = EncodeQueueEntry(
        id = name,
        original_filename = path,
    )
    entry.save()


class Command(BaseCommand):
    help = 'Watches the configured directories for now videos to encode'

    option_list = BaseCommand.option_list + (
        make_option('--foreground',
            action='store_false',
            dest='daemonize',
            default=True,
            help="Run foreground instead of daemonize"
        ),
    )

    def handle(self, *args, **options):
        watch(TAS_WATCHED_DIRECTORIES, TAS_VIDEO_EXTENSIONS, add_entry, options['daemonize'])
