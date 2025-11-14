import sys
from stats import get_num_words, get_book_text, get_num_characters
from helper import sort_on

def main():
        if len(sys.argv) < 2:
            print("Usage: python3 main.py <path_to_book>")
            sys.exit(1)

        path = sys.argv[1]
        text = get_book_text(path)
        print("============ BOOKBOT ============")
        print(f"Analyzing book fount at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {get_num_words(text)} total words")
        print("--------- Character Count -------")
        dict_characters = get_num_characters(text)
        dict_characters = list(dict_characters.items())
        dict_characters.sort(reverse=True, key=sort_on)
        for item in dict_characters:
            print(f"{item[0]}: {item[1]}")
        print("============= END ===============")
    
if __name__ == "__main__":
    main()