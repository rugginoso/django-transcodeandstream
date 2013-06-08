#!/usr/bin/env python

# Use setuptools if we can
try:
    from setuptools.core import setup
except ImportError:
    from distutils.core import setup
from transcodeandstream import __version__

setup(
    name='django-transcodeandstream',
    version=__version__,
    description='Transcode videos and stream with Django',
    long_description='Django Transcode & Stream permits to transcode, organize and stream videos using Django.',
    author='Lorenzo Masini',
    author_email='rugginoso@develer.com',
    url='http://github.com/rugginoso/django-transcodeandstream/',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2.7",
        "Topic :: Multimedia :: Video :: Conversion",
        "Topic :: Multimedia :: Video :: Display",
    ],
    packages=[
        'transcodeandstream',
        'transcodeandstream.migrations',
        'transcodeandstream.management',
        'transcodeandstream.management.commands',
    ],
    install_requires=[
        'django>=1.4',
        'south>=1.8',
        'pyinotify>=0.9',
    ]
)
