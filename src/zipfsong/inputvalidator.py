# coding=utf-8

import re

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
