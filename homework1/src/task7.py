import numpy as np

def average_numpy(numbers):
    """function that demonstrates the use of numpy 
    by converting a list of numbers to a numpy array and finding the average"""

    numpy_array = np.array(numbers)
    sum = 0
    count = 0
    for i in numpy_array:
        sum += i
        count += 1
    average = sum/count
    print(average)
    return average

numbers = [4,2,1,6,34,]
average_numpy(numbers)
