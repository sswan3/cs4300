from wonderwords import RandomWord
import random

def add_books(fav_list, books):
    fav_list.append(books)

def top_three(my_list):
    three_books = my_list[0:3]
    print(f"top three are: {three_books}")
    return three_books

def generate_student_base():
    student_database = {
        "Savannah": "316433",
        "Sam": "123543",
        "Alexander": "555439",
        "Bob": "660481",
        "Tammy": "390644",
    }
    return student_database

def add_to_student_base(name, num, dictionary):
    #if there is a missing name make a random name
    if name == "":
        r = RandomWord()
        random_name = r.word()
        dictionary[random_name] = num
        return dictionary
    #if the id is missing make a random one
    elif num == "":
        random_num = random.randint(100000, 999999)
        dictionary[name] = random_num
        return dictionary
    else:
        dictionary[name] = num
        return dictionary
        
def lookup_byname_student_base(name, dictionary):
    for n, num in dictionary.items():
        if n == name:
            print(n, num)
            return n, num

book1 = {"This Fatal Kiss": "Alicia Jasinska"}
book2 = { "The Setting Sun": "Osamu Dazai" }
book3 = {"Wings of Starlight": "Allison Saft"}
book4 = {"Daughter of the Moon Goddess": "Sue Lynn Tan"}
book5 = {"Mexican Gothic": "Silvia Moreno-Garcia"}
book6 = {"A Room of One's Own": "Virginia Woolf"}

fav_list = []
add_books(fav_list, book1)
add_books(fav_list, book2)
add_books(fav_list, book3)
add_books(fav_list, book4)
add_books(fav_list, book5)
add_books(fav_list, book6)

#print(fav_list)
#top_three(fav_list)

student_base = generate_student_base()
print(add_to_student_base("Peach", "555555", student_base))

