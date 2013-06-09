import time
import datetime
import re
import os
import select
from subprocess import Popen, PIPE


def time_to_seconds(time_string):
    try:
        t = time.strptime(time_string.split('.')[0], '%H:%M:%S')
    except ValueError:
        return 0

    d = datetime.timedelta(hours=t.tm_hour, minutes=t.tm_min, seconds=t.tm_sec)
    return d.total_seconds()


def parse_line(line):
    progress = 0
    duration = 0
    log = ""

    progress_regexp = re.compile(r'time=(\d\d:\d\d:\d\d.\d\d)')
    duration_regexp = re.compile(r'Duration:\s+(\d\d:\d\d:\d\d.\d\d)')

    m = progress_regexp.search(line)
    if m:
        try:
            progress = time_to_seconds(m.group(1))
        except IndexError:
            pass

    m = duration_regexp.search(line)
    if m:
        try:
            duration = time_to_seconds(m.group(1))
        except IndexError:
            pass

    if progress == 0 and duration == 0:
        log = line

    return (progress, duration, log)


def encode(id, original_filename, dest_dir, ffmpeg_executable,
           ffmpeg_options, progress_callback, finish_callback):
    cmdline = [ffmpeg_executable, '-i', original_filename]
    cmdline.extend(ffmpeg_options)
    cmdline.append(os.path.join(dest_dir, id + '.webm'))

    duration = 0
    transcoder = Popen(cmdline, stderr=PIPE, universal_newlines=True)
    status = None

    while status is None and select.select([transcoder.stderr.fileno()], [], []):
        p, d, l = parse_line(transcoder.stderr.readline())
        if not duration:
            duration = d
        progress = p / duration * 100 if duration else 0
        progress_callback(id, progress, l)
        status = transcoder.poll()

    finish_callback(id, status)
