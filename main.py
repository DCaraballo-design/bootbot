def main():
     file_path = "books/frankenstein.txt"
     text = get_book_text(file_path)
     print(text)

def get_book_text(path):
    # Use an absolute path to the file
    with open(path, "r", encoding='utf-8') as file:
        return file.read()
   
main()