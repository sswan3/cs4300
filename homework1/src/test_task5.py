from task5 import top_three
from task5 import favorite_books

#verify the top three list contains only three items
def test_count_top_three():
    favs_list = favorite_books()
    three = top_three(favs_list)
    count = 0
    for i in three:
        count += 1
    assert count == 3

#verify each single item in the list is made up of book, author
def test_author_books():
    
