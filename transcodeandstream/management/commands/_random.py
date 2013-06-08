from random import randrange


CHARACTERS_RANGE = [chr(n) for n in xrange(ord('a'), ord('z'))] \
                 + [chr(n) for n in xrange(ord('A'), ord('Z'))] \
                 + [chr(n) for n in xrange(ord('0'), ord('9'))] \
                 + ['_', '-']


def generate_random_unique_name(existing_names, length=10):
    while True:
        name = "".join([CHARACTERS_RANGE[randrange(0, len(CHARACTERS_RANGE) - 1)] for n in xrange(length)])
        if name not in existing_names:
            return name
