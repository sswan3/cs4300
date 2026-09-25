from task6 import word_count
from pathlib import Path
import pytest

@pytest.mark.parametrize("test_input, expected",
[
    ("task6_read_me_dogs.txt", 4),
    ("task6_read_me_food.txt", 7),
    ("task6_read_me_house.txt", 2),
]
)

def test_word_count_accuracy(test_input, expected):
    """verify word count is correct and function works for file that exists"""
    count = word_count(test_input)
    assert count == expected

def test_word_count_file_not_exist():
    """handling for a file that does not exist"""
    with pytest.raises(FileNotFoundError):
        count = word_count("task5_read_me.txt")

