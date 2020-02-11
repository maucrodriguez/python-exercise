def is_palindrome(text: str):
    text = [t.casefold() for t in text if t.isalpha()]
    return text == text[::-1]

