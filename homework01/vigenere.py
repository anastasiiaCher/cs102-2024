"""
Encrypts and decrypts a text using Vigenere cipher.
"""


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    for i, symbol in enumerate(plaintext):
        if symbol.isalpha() and symbol.isupper():
            shift = ord(keyword[i % len(keyword)].upper()) - 65
            ciphertext += chr(ord(symbol) + shift) if ord(symbol) + shift < 91 else chr(ord(symbol) + shift - 26)
        elif symbol.isalpha() and symbol.islower():
            shift = ord(keyword[i % len(keyword)].lower()) - 97
            ciphertext += chr(ord(symbol) + shift) if ord(symbol) + shift < 123 else chr(ord(symbol) + shift - 26)
        else:
            ciphertext += symbol
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    for i, symbol in enumerate(ciphertext):
        if symbol.isalpha() and symbol.isupper():
            shift = ord(keyword[i % len(keyword)].upper()) - 65
            plaintext += chr(ord(symbol) - shift) if ord(symbol) - shift > 64 else chr(ord(symbol) - shift + 26)
        elif symbol.isalpha() and symbol.islower():
            shift = ord(keyword[i % len(keyword)].lower()) - 97
            plaintext += chr(ord(symbol) - shift) if ord(symbol) - shift > 96 else chr(ord(symbol) - shift + 26)
        else:
            plaintext += symbol
    return plaintext
