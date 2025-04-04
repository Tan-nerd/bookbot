def word_count(text):
    word_list = text.split()
    return len(word_list)

def get_letter_count(words):
    letter_count = {}
    book_lowercase = words.lower()
    for letter in book_lowercase:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count

def sort_on(dict):
    return dict["count"]

def sort_dict(dikt):
    char_list = []
    temp_dict = {}
    for letter in dikt:
        temp_dict = {"letter" : letter, "count" : dikt[letter]}
        char_list.append(temp_dict)    
    char_list.sort(reverse=True, key=sort_on)
    return char_list
    