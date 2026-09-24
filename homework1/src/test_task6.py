from task6 import word_count

#verify word count is correct
def test_word_count_accuracy():
    count = word_count()
    assert count == 104