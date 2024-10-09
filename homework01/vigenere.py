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
                shift = ord(keyword[i % len(keyword)]) - 13 % 26
                temp = chr(65 + (((ord(char) - 13) % 26 + shift) % 26))
            else:
                shift = ord(keyword[i % len(keyword)]) - 19 % 26
                temp = chr(97 + (((ord(char) - 19) % 26 + shift) % 26))
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
                shift = ord(keyword[i % len(keyword)]) - 13 % 26
                temp = chr(65 + (((ord(char) - 13) % 26 - shift) % 26))
            else:
                shift = ord(keyword[i % len(keyword)]) - 19 % 26
                temp = chr(97 + (((ord(char) - 19) % 26 - shift) % 26))
            plaintext += temp
        else:
            plaintext += char
    return plaintext
