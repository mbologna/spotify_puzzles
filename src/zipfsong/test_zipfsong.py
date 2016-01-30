import pytest
from zipfsong import Song
from zipfsong import ZipfSong
from zipfsong import Parser

def test_case_1():
    input_str = """4 2
    30 one
    30 two
    15 three
    25 four
    """
    expected = [Song(4, "four", 25), Song(2, "two", 30)]

    N_TRACKS_TO_SELECT = Parser.parse_input_first_line(input_str.split("\n")[0])[1]
    TRACKLIST = input_str.split("\n")[1:]
    TRACKLIST = map(str.strip, TRACKLIST)
    TRACKLIST = [track for track in TRACKLIST if track != '']

    assert ZipfSong.extract_top_k_songs(N_TRACKS_TO_SELECT, TRACKLIST) == expected

def test_case_2():
    input_str = """15 3
    197812 re_hash
    78906 5_4
    189518 tomorrow_comes_today
    39453 new_genious
    210492 clint_eastwood
    26302 man_research
    22544 punk
    19727 sound_check
    17535 double_bass
    18782 rock_the_house
    198189 19_2000
    13151 latin_simone
    12139 starshine
    11272 slow_country
    10521 m1_a1
    """
    expected = [Song(11, "19_2000", 198189),
                Song(5, "clint_eastwood", 210492),
                Song(3, "tomorrow_comes_today", 189518)]

    N_TRACKS_TO_SELECT = Parser.parse_input_first_line(input_str.split("\n")[0])[1]
    TRACKLIST = input_str.split("\n")[1:]
    TRACKLIST = map(str.strip, TRACKLIST)
    TRACKLIST = [track for track in TRACKLIST if track != '']

    assert ZipfSong.extract_top_k_songs(N_TRACKS_TO_SELECT, TRACKLIST) == expected

def test_case_3():
    input_str = """6 6
    60 one
    30 two
    20 three
    15 four
    12 five
    10 six"""

    expected = [Song(1, "one", 60),
                Song(2, "two", 30),
                Song(3, "three", 20),
                Song(4, "four", 15),
                Song(5, "five", 12),
                Song(6, "six", 10)]

    N_TRACKS_TO_SELECT = Parser.parse_input_first_line(input_str.split("\n")[0])[1]
    TRACKLIST = input_str.split("\n")[1:]
    TRACKLIST = map(str.strip, TRACKLIST)
    TRACKLIST = [track for track in TRACKLIST if track != '']

    assert ZipfSong.extract_top_k_songs(N_TRACKS_TO_SELECT, TRACKLIST) == expected

def test_case_4():
    input_str = """6 3
    60 one
    30 two
    20 three
    15 four
    120 five
    100 six"""

    expected = [Song(5, "five", 120),
                Song(6, "six", 100),
                Song(1, "one", 60)]

    N_TRACKS_TO_SELECT = Parser.parse_input_first_line(input_str.split("\n")[0])[1]
    TRACKLIST = input_str.split("\n")[1:]
    TRACKLIST = map(str.strip, TRACKLIST)
    TRACKLIST = [track for track in TRACKLIST if track != '']

    assert ZipfSong.extract_top_k_songs(N_TRACKS_TO_SELECT, TRACKLIST) == expected

def test_case_exception():
    input_str = """50001 50001
    10 abc"""

    with pytest.raises(ValueError) as exc:
        N_TRACKS_TO_SELECT = Parser.parse_input_first_line(input_str.split("\n")[0])[1]
        assert exc.value.args[0] == "number of songs out of boundaries"
