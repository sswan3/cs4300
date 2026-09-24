from task2 import information
import pytest
my_list = information()
@pytest.mark.parametrize("test_input, expected",
[
    (my_list[0], str),
    (my_list[1], int),
    (my_list[2], bool),
    (my_list[3], float)

]
)

def test_information(test_input, expected):
    assert isinstance(test_input, expected)
