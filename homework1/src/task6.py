import string
def word_count():
    """function that reads from a file and counts the words and returns the word count"""
    count = 0
    list = []
    list2 = []

    with open("task6_read_me.txt", "r", encoding="utf-8") as file:
        for line in file:
            # Split each line into individual words
            for word in line.split():
                list.append(word)

    for i in list:
        # .strip() strips any hidden newline or carriage return characters first
        clean = i.strip().translate(str.maketrans("", "", string.punctuation))
        if clean:  # skips adding empty strings if a token was strictly punctuation (like "." or ",")
            list2.append(clean)


    word_count = len(list2)
    print(word_count)
    return word_count