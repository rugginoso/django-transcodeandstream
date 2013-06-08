import os
from pyinotify import WatchManager, Notifier, ProcessEvent, IN_CREATE, IN_MOVED_TO


def check_extension(path, extensions):
    _, ext = os.path.splitext(path)
    return (ext and ext in extensions)


def scan_dir(path, extensions):
    videos_paths = []
    for dirname, dirnames, filenames in os.walk(path):
        videos_paths.extend([os.path.join(path, dirname, filename) for filename in filenames if check_extension(filename, extensions)])
    return videos_paths


def process_new_entry(path, is_dir, extensions, callback):
    videos_paths = []
    if is_dir:
        videos_paths.extend(scan_dir(path, extensions))
    else:
        if check_extension(path, extensions):
            videos_paths.append(path)

    for video_path in videos_paths:
        callback(video_path)


class EventHandler(ProcessEvent):
    def __init__(self, callback, extensions, *args, **kwargs):
        self.callback = callback
        self.extensions = extensions
        super(EventHandler, self).__init__(*args, **kwargs)

    def process_IN_CREATE(self, event):
        process_new_entry(event.pathname, event.dir, self.extensions, self.callback)

    def process_IN_MOVED_TO(self, event):
        process_new_entry(event.pathname, event.dir, self.extensions, self.callback)


def watch(dirs, extensions, callback, daemonize=False):
    wm = WatchManager()
    notifier = Notifier(wm, EventHandler(callback, extensions))
    for d in dirs:
        wm.add_watch(d, IN_CREATE | IN_MOVED_TO)
    notifier.loop(daemonize=daemonize)