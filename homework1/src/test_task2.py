from task2 import information
import pytest

@pytest.mark.parametrize("item", information())
def test_information(item):
    is_valid_type = isinstance(item, (str, int, float, bool))