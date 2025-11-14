def get_book_text(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None

def get_num_words(text):
    return len(text.split())

def get_num_characters(text):
    text = text.lower()
    characters = {}
    for char in text:
        if char.isalpha():
            characters[char] = characters.get(char, 0) + 1
    return characters

