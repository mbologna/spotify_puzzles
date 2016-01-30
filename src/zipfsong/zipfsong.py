# coding=utf-8
import sys
from .song import Song
from .zipfclassifier import ZipfClassifier
from .inputparser import Parser

class ZipfSong(object):
    def __init__(self):
        pass

    @staticmethod
    def extract_top_k_songs(input_str):
        number_of_album_songs, number_of_songs_to_select = \
            Parser.parse_input_first_line(input_str.split('\n')[0])
        zipfc = ZipfClassifier(number_of_songs_to_select)
        for j in range(0, number_of_album_songs, 1):
            line = input_str.split("\n")[j + 1].strip()
            listen_count, track_name = \
                Parser.parse_values_separated_by_space(line)
            song_to_add = Song(j + 1, track_name, listen_count)
            zipfc.add_song(song_to_add)
        return zipfc.retrieve_n_top_quality_songs()

if __name__ == "__main__":
    ALBUM_TRACKS = sys.stdin.readline()
    TRACKLIST = ""
    N_TRACKS = int(ALBUM_TRACKS.split(" ")[0])
    for i in range(0, N_TRACKS, 1):
        TRACKLIST += sys.stdin.readline()
    for song in ZipfSong.extract_top_k_songs(ALBUM_TRACKS + TRACKLIST):
        print(song)
