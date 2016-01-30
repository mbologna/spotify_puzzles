# coding=utf-8

from .inputvalidator import InputValidator

class Song(object):
    def __init__(self, index, name, listen_count):
        InputValidator.validate_listen_count(listen_count)
        InputValidator.validate_track_name(name)
        self.index = index
        self.name = name
        self.listen_count = listen_count
        self.quality = listen_count * index
        # Specifically, suppose that song i has been played fi times but that
        # Zipf’s Law predicts that it would have been played zi times. Then you
        # define the quality of song i to be qi = fi / zi, where zi = 1/i

    def __str__(self):
        return self.name

    def __repr__(self):
        return  "name: " + self.name + ", index: " + str(self.index) + \
                ", quality: " + str(self.quality)

    def get_index(self):
        return self.index

    def get_quality(self):
        return self.quality

    # If two songs have the same quality, give precedence to the one
    # appearing first on the album (presumably there was a reason for the
    # producers to put that song before the other).
    def __lt__(self, other):
        if self.get_quality() == other.get_quality():
            return self.get_index() < other.get_index()
        else:
            # heapq is a min-heap, so a song is lt than another if it has
            # a greater quality (inverted!)
            return self.get_quality() > other.get_quality()

    def __eq__(self, other):
        return self.get_quality() == other.get_quality() and \
               self.get_index() == other.get_index()

