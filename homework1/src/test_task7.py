from task7 import average_numpy
import numpy as np

def test_average_numpy():
    numbers = [4,2,1,6,34,]
    average = average_numpy(numbers)
    assert average == 9.4