import numpy as np

def average_numpy(numbers):
    """function that demonstrates the use of numpy by finding the average"""
    average = np.mean(numbers)
    return average

def min_numpy(numbers):
    smallest_value = np.min(numbers)
    return smallest_value

numbers = [4,2,1,6,34,]
print(average_numpy(numbers))
print(min_numpy(numbers))
