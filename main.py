text = ""

def get_book_text():
    # Use an absolute path to the file
    file_path = r"\books\frankenstein.txt"
    with open(file_path, "r", encoding='utf-8') as file:
        content = file.read()
        print(content)

def main():
    # Call the function to get the book text
    get_book_text()

main()