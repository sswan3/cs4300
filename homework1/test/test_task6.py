from task6 import word_count
from pathlib import Path
import pytest


def test_word_count_accuracy():
    """verify word count is correct and function works for file that exists"""
    count = word_count("task6_read_me.txt")
    assert count == 104

def test_word_count_file_not_exist():
    """handling for a file that does not exist"""
    with pytest.raises(FileNotFoundError):
        count = word_count("task5_read_me.txt")

