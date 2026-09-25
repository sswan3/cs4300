from task5 import top_three
from task5 import add_to_student_base
from task5 import lookup_byname_student_base
from task5 import generate_student_base
from task5 import add_books


#verify the top three list contains only three items
def test_count_top_three():
    book1 = {"This Fatal Kiss": "Alicia Jasinska"}
    book2 = { "The Setting Sun": "Osamu Dazai" }
    book3 = {"Wings of Starlight": "Allison Saft"}
    book4 = {"Daughter of the Moon Goddess": "Sue Lynn Tan"}
    fav_list = []

    add_books(fav_list, book1)
    add_books(fav_list, book2)
    add_books(fav_list, book3)
    add_books(fav_list, book4)
    
    three = top_three(fav_list)

    assert three == fav_list[0:3]

def test_add_student_base():
    base = generate_student_base()
    add_to_student_base("Peach", "555555", base)
    if "Peach" in base:
        print("value found")

def test_add_with_missing_values():
    base = generate_student_base()
    add_to_student_base("", "555555", base)
    






    
