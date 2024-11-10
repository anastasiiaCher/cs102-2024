"""
Модуль для реализации шифра Виженера.
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
    keyword_repeated = (keyword * (len(plaintext) // len(keyword) + 1))[: len(plaintext)]

    for p_char, k_char in zip(plaintext, keyword_repeated):
        if p_char.isalpha():
            shift = ord(k_char.upper()) - ord("A")
            base = ord("A") if p_char.isupper() else ord("a")
            encrypted_char = chr((ord(p_char) - base + shift) % 26 + base)
            ciphertext += encrypted_char
        else:
            ciphertext += p_char
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
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword) + 1))[: len(ciphertext)]

    for c_char, k_char in zip(ciphertext, keyword_repeated):
        if c_char.isalpha():
            shift = ord(k_char.upper()) - ord("A")
            base = ord("A") if c_char.isupper() else ord("a")
            decrypted_char = chr((ord(c_char) - base - shift) % 26 + base)
            plaintext += decrypted_char
        else:
            plaintext += c_char

    return plaintext
