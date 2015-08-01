# coding=utf-8
__author__ = 'Michele Bologna'

import sys
import heapq
import re


class Parser(object):
    @staticmethod
    def parse_values_separated_by_space(str):
        left = str.split(" ")[0]
        right = str.split(" ")[1]
        return left, right


class IO(object):
    @staticmethod
    def readline():
        return sys.stdin.readline()


class InputValidator(object):
    # Each song name is at most 30 characters long and consists only of the characters:
    # ‘a’-‘z’, ‘0’-‘9’, and underscore (‘_’)
    valid_string_pattern = re.compile('^[a-z0-9_]*$')

    @staticmethod
    def validate_number_of_songs(m, n):
        # (1 ≤ n ≤ 50000, 1 ≤ m ≤ n)
        return 1 <= n <= 50000 and 1 <= m <= n

    @staticmethod
    def validate_listen_count(fi):
        # fi: 0 ≤ fi ≤ 10^12 is the number of times the i’th song was listened to
        validation = (0 <= fi <= 10 ** 12)
        if not validation:
            raise ValueError("listen count out of boundaries: " + fi)

    @staticmethod
    def validate_track_name(track_name):
        if len(track_name) <= 30 and InputValidator.valid_string_pattern.search(track_name) is not None:
            return True
        raise ValueError("track name not correct: " + track_name)


class Song(object):
    def __init__(self, index, name, listen_count):
        InputValidator.validate_listen_count(listen_count)
        InputValidator.validate_track_name(track_name)
        self.index = index
        self.name = name
        self.listen_count = listen_count
        self.quality = listen_count * index  # Specifically, suppose that song i has been played fi times but that Zipf’s Law predicts that it would have been played zi times. Then you define the quality of song i to be qi = fi / zi, where zi = 1/i

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.names

    def quality(self):
        return self.quality


class ZipfClassifier:
    def __init__(self, capacity):
        self.songs = []
        self.capacity = capacity

    def add_song(self, song):
        # heapq is a min-heap, so we should reverse the quality index (* -1)
        heapq.heappush(self.songs, (-song.quality, song.index, song))

    def retrieve_n_top_quality_songs(self):
        return heapq.nsmallest(self.capacity, self.songs)


input_str = IO.readline()
number_of_album_songs, number_of_songs_to_select = Parser.parse_values_separated_by_space(input_str)
number_of_album_songs = int(number_of_album_songs)  # n = Album's number_of_songs
number_of_songs_to_select = int(number_of_songs_to_select)  # m = number of songs to select
if InputValidator.validate_number_of_songs(number_of_songs_to_select, number_of_album_songs):
    zipfclassifier = ZipfClassifier(number_of_songs_to_select)
    for i in xrange(0, number_of_album_songs, 1):
        line = IO.readline().strip()
        listen_count, track_name = Parser.parse_values_separated_by_space(line)
        listen_count = int(listen_count)
        song = Song(i + 1, track_name, listen_count)
        zipfclassifier.add_song(song)
    for song in zipfclassifier.retrieve_n_top_quality_songs():
        print(song[2])
else:
    raise ValueError("Error during parsing: value out of boundaries (" + str(number_of_songs_to_select) + "," + str(
        number_of_album_songs) + ")")

