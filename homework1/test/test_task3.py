from task3 import positive_or_negative
from task3 import sum_num
from task3 import prime_num
import pytest

#verifying that the numbers are only ints or floats------
def test_check_with_int():
    val = positive_or_negative(7)
    assert type(val) in (float, int)

def test_check_with_float():
    val = positive_or_negative(8.12)
    assert type(val) in (float, int)
#---------------------------------------------------------

#verifying that the results of positive_or_negative are accurate..................................
@pytest.mark.parametrize("test_input, expected",
[
    (4, "positive\n"), #testing for positive number
    (-3, "negative\n"), #testing for negative number
    (0, "zero\n"),       #testing for number 0
    (-0.0003, "negative\n"), #test negative float
    (0.5, "positive\n") #test positive float
]
)
#capture output and compare to correct answer
def test_positive_or_negative_output(capsys, test_input, expected): 
    positive_or_negative(test_input)
    captured = capsys.readouterr()
    assert captured.out == expected
#...........................................................................................
 
#verifying that the sum is correct
def test_sum_num():
    val = sum_num()
    assert val == 5050

#making sure that first and last elements of prime numbers are correct
def test_first_and_last_prime():
    my_list = prime_num()
    assert my_list[0] == 2 and my_list[-1] == 29

#Make sure 0 or 1 are not counted as prime numbers
def test_Zero_and_One_Trap():
    my_list = prime_num()
    found_error = False
    if 0 in my_list or 1 in my_list:
        found_error = True
    assert found_error == False

    
#verifying that the first 10 prime numbers are correct
def test_prime_num():
    val = prime_num()
    assert val == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    




