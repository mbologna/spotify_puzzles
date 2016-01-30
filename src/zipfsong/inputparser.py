from inputvalidator import InputValidator

class Parser(object):
    @staticmethod
    def parse_values_separated_by_space(string):
        left = string.split(" ")[0]
        right = string.split(" ")[1]
        return int(left), right # first input value is always a number

    @staticmethod
    def parse_input_first_line(input_str):
        number_of_album_songs, number_of_songs_to_select = \
            Parser.parse_values_separated_by_space(input_str)
        number_of_album_songs = int(number_of_album_songs)
        # n = Album number_of_songs
        number_of_songs_to_select = int(number_of_songs_to_select)
        # m = number of songs to select
        InputValidator.validate_number_of_songs(number_of_songs_to_select,
                                                number_of_album_songs)
        return number_of_album_songs, number_of_songs_to_select
