import sys
from stats import count_words, count_characters,sort_characters

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

def main():
    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    if "Error" in book_text:
        print(book_text)
    else:
        num_words = count_words(book_text)
        #print(f"{num_words} words found in the document")

        char_counts = count_characters(book_text)
        #print("Character frequency in the document:")
        #print(char_counts)
        sorted_characters = sort_characters(char_counts)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {file_path}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        
        for item in sorted_characters:
            print(f"{item['character']}: {item['count']}")

        print("============= END ===============")

main()