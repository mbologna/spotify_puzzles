__author__ = 'Michele Bologna'

import rbn


def test_convert_to_bin():
    assert rbn.NumberConverter.dec_to_bin('42') == '101010'


def test_convert_to_dec():
    assert rbn.NumberConverter.bin_to_dec('101010') == 42


def test_convert_to_dec_to_bin():
    assert rbn.NumberConverter.dec_to_bin(rbn.NumberConverter.bin_to_dec('101010')) == '101010'


def test_convert_to_bin_to_dec():
    assert rbn.NumberConverter.bin_to_dec(rbn.NumberConverter.dec_to_bin('42')) == 42


def test_case_1():
    assert rbn.ReversedBinaryNumber.convert(13) == 11


def test_case_2():
    assert rbn.ReversedBinaryNumber.convert(47) == 61