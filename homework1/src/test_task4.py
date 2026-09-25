from task4 import calculate_discount
import pytest


def test_ints_only():
    #test with only ints
    result1 = calculate_discount(20, 15)
    assert result1 == 17

def test_int_float():
    #test with int, float
    result2 = calculate_discount(30, 15.25)
    assert result2 == 25.43

def test_float_int():
    #test with float, int
    result3 = calculate_discount(17.36, 2)
    assert result3 == 17.01

def test_float_only():
    #test with float, float
    result4 = calculate_discount(12.90, 4.321)
    assert result4 == 12.34

def test_many_decimal_places():
    #test with floats with many decimal places
    result5 = calculate_discount(13.3333999700, 5.22220201)
    assert result5 == 12.64

def test_negative_price():
    with pytest.raises(ValueError):
        calculate_discount(-60, 30)

def test_negative_discount():
    with pytest.raises(ValueError):
        calculate_discount(60, -30)

def test_big_discount():
    with pytest.raises(ValueError):
        calculate_discount(35.50, 250)

def test_not_number_price():
    letter = "s"
    with pytest.raises(TypeError):
        calculate_discount(letter, 60)

def test_not_number_discount():
    letter = "say hi"
    with pytest.raises(TypeError):
        calculate_discount(60, letter)




    

