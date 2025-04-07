from stats import word_count
from stats import char_count
from stats import riordina
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    #print(get_book_text("sys.argv[1]"))
    #print(f"{word_count("sys.argv[1]")} words found in the document")
    
    if len(sys.argv) != 2 :
        print("Il comando deve contenere 2 arg -> Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(sys.argv[1])} total words")
    print("--------- Character Count -------")

    conteggio = char_count(f"{sys.argv[1]}")
    conteggiordinato = riordina(conteggio)
    for i in conteggiordinato:
        print(f"{i['char']}: {i['count']}")

    print("============= END ===============")

main()