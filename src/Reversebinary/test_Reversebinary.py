__author__ = 'Michele Bologna'

import pytest

from src.Reversebinary import Reversebinary


def test_convert_to_bin():
    assert Reversebinary.NumberConverter.dec_to_bin(42) == '101010'


def test_convert_to_dec():
    assert Reversebinary.NumberConverter.bin_to_dec('101010') == 42


def test_convert_to_dec_to_bin():
    assert Reversebinary.NumberConverter.dec_to_bin(Reversebinary.NumberConverter.bin_to_dec('101010')) == '101010'


def test_convert_to_bin_to_dec():
    assert Reversebinary.NumberConverter.bin_to_dec(Reversebinary.NumberConverter.dec_to_bin(42)) == 42


def test_case_1():
    assert Reversebinary.ReversedBinaryNumber.convert(13) == 11


def test_case_2():
    assert Reversebinary.ReversedBinaryNumber.convert(47) == 61


def test_case_3():
    with pytest.raises(NotImplementedError) as exc:
        Reversebinary.ReversedBinaryNumber.convert(1000000001)
    assert exc.value.args[0] == "IT'S OVER 9000!!!111one"


def test_case_4():
    with pytest.raises(ValueError) as exc:
        Reversebinary.ReversedBinaryNumber.convert('aaa')
    assert 'error during conversion' in str(exc.value)
