from task2 import information
import pytest

#@pytest.mark.parametrize("item", information())
#def test_information(item):
    #is_valid_type = isinstance(item, (str, int, float, bool))

def test_correct_str():
    my_list = information()
    assert type(my_list[0]) == str

def test_correct_int():
    my_list = information()
    assert type(my_list[1]) == int


def test_correct_boolean():
    my_list = information()
    assert type(my_list[2]) == bool

def test_correct_float():
    my_list = information()
    assert type(my_list[3]) == float

