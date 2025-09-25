from stats import words, characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    count = words(text)
    print(f"Found {count} total words")
    letters = characters(text)
    print(letters)

main()