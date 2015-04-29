__author__ = 'Michele Bologna'


class NumberConverter(object):
    BASE = 2

    @staticmethod
    def dec_to_bin(number):
        return bin(number)[2:]  # bin outputs to '2b...'

    @staticmethod
    def bin_to_dec(number):
        return int(number, NumberConverter.BASE)


class ReversedBinaryNumber(object):
    @staticmethod
    def convert(number):
        try:
            number = int(number)
            if 1 <= number <= 1000000000:
                number_bin = NumberConverter.dec_to_bin(number)
                number_bin_reverse = number_bin[::-1]
                output_number_dec = NumberConverter.bin_to_dec(number_bin_reverse)
                return output_number_dec
            else:
                raise NotImplementedError("IT'S OVER 9000!!!111one")
        except ValueError:
            raise ValueError('error during conversion')



if __name__ == '__main__':
    try:
        input_number = raw_input('Insert a number: ')
        output_number = ReversedBinaryNumber.convert(input_number)
        print(output_number)
    except ValueError:
        print "nice try"

