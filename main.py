from stats import get_letter_count, word_count, sort_dict


def get_book_text(book_path):
    with open(book_path) as f:
        book = f.read()
    return book



def main():
    path = "./books/frankenstein.txt"
    num_words = word_count(get_book_text(path))
    sorted_letter_count = sort_dict(get_letter_count(get_book_text(path)))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print("Found", num_words, "total words")
    print("--------- Character Count -------")
    for i in range(len(sorted_letter_count)):
        if sorted_letter_count[i]["letter"].isalpha():
            alpha = sorted_letter_count[i]["letter"]
            num = sorted_letter_count[i]["count"]
            print(f"{alpha}: {num}")
    print("============= END ===============")
   
main()

