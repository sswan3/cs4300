import random
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
    val = calculate_discount(-70,4)
    assert val == "price must be positive"

def test_negative_discount():
    val = calculate_discount(50, -25)
    assert val == "discount must be positive"

def test_big_discount():
    val = calculate_discount(50, 250)
    assert val == "discount must be less than 100"

def test_not_number_price():
    letter = "s"
    val = calculate_discount(letter, 250)
    assert val == "error must be number"



    

