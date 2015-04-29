__author__ = 'Michele Bologna'


class NumberConverter(object):
    BASE = 2

    @staticmethod
    def dec_to_bin(number_as_str):
        try:
            return bin(int(number_as_str))[2:]  # bin outputs to '2b...'
        except ValueError:
            raise ValueError('error during conversion')

    @staticmethod
    def bin_to_dec(number_as_str):
        return int(number_as_str, NumberConverter.BASE)


class ReversedBinaryNumber(object):
    @staticmethod
    def convert(number):
        number_bin = NumberConverter.dec_to_bin(number)
        number_bin_reverse = number_bin[::-1]
        output_number_dec = NumberConverter.bin_to_dec(number_bin_reverse)
        return output_number_dec


if __name__ == '__main__':
    try:
        input_number = raw_input('Insert a number: ')
        output_number = ReversedBinaryNumber.convert(input_number)
        print(output_number)
    except ValueError:
        print "nice try"

