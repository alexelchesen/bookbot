from stats import get_num_words, get_char_counts, formatted_dicts
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content 

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    contents = get_book_text(filepath)
    num_words = get_num_words(contents)
    char_counts = get_char_counts(contents)
    formatted_char_counts = formatted_dicts(char_counts)
    report = "============ BOOKBOT ============\n" + \
                f"Analyzing book at {filepath}...\n" + \
                "----------- Word Count ----------\n" + \
                f"Found {num_words} total words\n" + \
                "--------- Character Count -------\n"
    for char_dict in formatted_char_counts:
        if char_dict["char"].isalpha():
            report += f"{char_dict["char"]}: {char_dict["num"]}\n"
    report += "============= END ==============="
    print(report)




if __name__ == "__main__":
    main()