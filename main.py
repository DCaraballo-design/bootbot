def main():
     from stats import word_count
     file_path = "books/frankenstein.txt"
     text = get_book_text(file_path)
     num_words = len(word_count(text))
     print(f"{num_words} words found in the document")

def get_book_text(path):
    # Use an absolute path to the file
    with open(path, "r", encoding='utf-8') as file:
        return file.read()
   
main()