from django.core.management.base import BaseCommand, CommandError
from optparse import make_option

from transcodeandstream.models import EncodeQueueEntry
from transcodeandstream.settings import TAS_WATCHED_DIRECTORIES, TAS_VIDEO_EXTENSIONS, TAS_TRANSCODER_FORMATS

from _watcher import watch, initial_check
from _random import generate_random_unique_name


def add_entry(path):
    if EncodeQueueEntry.objects.filter(original_filename=path).count() == 0:
        existing_names = [entry['id']
                          for entry in EncodeQueueEntry.objects.values('id')]
        name = generate_random_unique_name(existing_names)

        for format in TAS_TRANSCODER_FORMATS:
            entry = EncodeQueueEntry(
                id=name,
                original_filename=path,
                transcode_format=format,
            )
            entry.save()


class Command(BaseCommand):
    help = 'Watches the configured directories for now videos to encode'

    def handle(self, *args, **options):
        paths_just_there = set([entry['original_filename']
                            for entry in EncodeQueueEntry.objects.get_new_entries().values('original_filename')])
        initial_check(
            paths_just_there,
            TAS_WATCHED_DIRECTORIES,
            TAS_VIDEO_EXTENSIONS,
            add_entry)
        watch(TAS_WATCHED_DIRECTORIES, TAS_VIDEO_EXTENSIONS, add_entry)
