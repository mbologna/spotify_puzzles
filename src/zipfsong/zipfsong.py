# coding=utf-8
import sys
import heapq
import re

class Parser(object):
    @staticmethod
    def parse_values_separated_by_space(string):
        left = string.split()[0]
        right = string.split()[1]
        return long(left), right # first input value is always a number

    @staticmethod
    def parse_input_first_line(input_str):
        number_of_album_songs, number_of_songs_to_select = \
            Parser.parse_values_separated_by_space(input_str)
        number_of_songs_to_select = long(number_of_songs_to_select)
        # m = number of songs to select
        InputValidator.validate_number_of_songs(number_of_songs_to_select,
                                                number_of_album_songs)
        return number_of_album_songs, number_of_songs_to_select


class InputValidator(object):
    # Each song name is at most 30 characters long and consists only of the
    # characters:
    # ‘a’-‘z’, ‘0’-‘9’, and underscore (‘_’)
    valid_string_pattern = re.compile('^[a-z0-9_]*$')

    @staticmethod
    def validate_number_of_songs(number_of_songs_to_select, number_of_album_songs):
        # (1 ≤ n ≤ 50000, 1 ≤ m ≤ n)
        if not (1 <= number_of_album_songs <= 50000 and \
                1 <= number_of_songs_to_select <= number_of_album_songs):
            raise ValueError("number of songs out of boundaries")

    @staticmethod
    def validate_listen_count(listen_frequency):
        validation = (0 <= listen_frequency <= 10 ** 12)
        # fi: 0 ≤ fi ≤ 10^12 is the number of times the i’th song was listened
        # to
        if not validation:
            raise ValueError("listen count out of boundaries: " + listen_frequency)

    @staticmethod
    def validate_track_name(track_name):
        if len(track_name) <= 30 and \
        InputValidator.valid_string_pattern.search(track_name) is not None:
            return True
        raise ValueError("track name not correct: " + track_name)


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

    # If two songs have the same quality, give precedence to the one
    # appearing first on the album (presumably there was a reason for the
    # producers to put that song before the other).
    def __lt__(self, other):
        if self.quality == other.quality:
            return self.index < other.index
        else:
            # heapq is a min-heap, so a song is lt than another if it has
            # a greater quality (inverted!)
            return self.quality > other.quality

    def __eq__(self, other):
        return self.quality == other.quality and \
               self.index == other.index

class ZipfClassifier(object):
    def __init__(self, capacity):
        self.songs = []
        self.capacity = capacity

    def add_song(self, song_to_add):
        self.songs.append(song_to_add)

    def retrieve_n_top_quality_songs(self):
        return heapq.nsmallest(self.capacity, self.songs)

class ZipfSong(object):
    def __init__(self):
        pass

    @staticmethod
    def extract_top_k_songs(number_of_songs_to_select, tracklist):
        zipfc = ZipfClassifier(number_of_songs_to_select)
        track_no = 1
        for track in tracklist:
            listen_count, track_name = \
                Parser.parse_values_separated_by_space(track)
            song_to_add = Song(track_no, track_name, listen_count)
            zipfc.add_song(song_to_add)
            track_no += 1
        return zipfc.retrieve_n_top_quality_songs()

if __name__ == "__main__":
    ALBUM_TRACKS = sys.stdin.readline()
    TRACKLIST = []
    N_TRACKS, N_TRACKS_TO_SELECT = Parser.parse_input_first_line(ALBUM_TRACKS)
    for i in range(0, N_TRACKS, 1):
        TRACKLIST.append(sys.stdin.readline())
    TOP_K_SONGS = ZipfSong.extract_top_k_songs(N_TRACKS_TO_SELECT, TRACKLIST)
    for song in TOP_K_SONGS:
        print(song)
