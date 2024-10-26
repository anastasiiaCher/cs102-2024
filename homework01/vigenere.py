"""
Module executing the Vigenere cipher
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
    for i, char in enumerate(plaintext):
        if char.isalpha():
            if char.isupper():
                shift = ord(keyword[i % len(keyword)]) - ord("A")
                temp = chr(ord("A") + (ord(char) - ord("A") + shift) % 26)
            else:
                shift = ord(keyword[i % len(keyword)]) - ord("a")
                temp = chr(ord("a") + (ord(char) - ord("a") + shift) % 26)
            ciphertext += temp
        else:
            ciphertext += char
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
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            if char.isupper():
                shift = ord(keyword[i % len(keyword)]) - ord("A")
                temp = chr(ord("A") + (ord(char) - ord("A") - shift) % 26)
            else:
                shift = ord(keyword[i % len(keyword)]) - ord("a")
                temp = chr(ord("a") + (ord(char) - ord("a") - shift) % 26)
            plaintext += temp
        else:
            plaintext += char
    return plaintext
