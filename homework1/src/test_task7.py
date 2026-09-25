from task7 import average_numpy
from task7 import min
import numpy as np

def test_average_numpy():
    numbers = [4,2,1,6,34]
    average = average_numpy(numbers)
    sum = 0
    count = 0
    for i in numbers:
        sum += i
        count += 1
    test_average = sum/count
    assert average == test_average

def test_min():
    numbers = [4,2,1,6,34]
    numpy_min = min(numbers)

    min_test = numbers[0]
    for i in numbers:
        if i < min_test:
            min_test = i
    assert numpy_min == min_test




