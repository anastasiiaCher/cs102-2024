"""Алгоритм позволяет зашифровать и расшифровать сообщение при помощи шифра Виженера."""


ALPHA = "abcdefghijklmnopqrstuvwxyz"
ALPHA_CAPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


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
    keyword_new = keyword * (len(plaintext) // len(keyword))
    keyword_new += keyword[: (len(plaintext) % len(keyword))]

    for pos, symbol in enumerate(plaintext):
        if symbol in ALPHA:
            ciphertext += ALPHA[(ALPHA.find(symbol) + ALPHA.find(keyword_new[pos])) % len(ALPHA)]
        elif symbol in ALPHA_CAPS:
            ciphertext += ALPHA_CAPS[(ALPHA_CAPS.find(symbol) + ALPHA_CAPS.find(keyword_new[pos])) % len(ALPHA_CAPS)]
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
    keyword_new = keyword * (len(ciphertext) // len(keyword))
    keyword_new += keyword[: (len(ciphertext) % len(keyword))]

    for pos, symbol in enumerate(ciphertext):
        if symbol in ALPHA:
            plaintext += ALPHA[(ALPHA.find(symbol) - ALPHA.find(keyword_new[pos])) % len(ALPHA)]
        elif symbol in ALPHA_CAPS:
            plaintext += ALPHA_CAPS[(ALPHA_CAPS.find(symbol) - ALPHA_CAPS.find(keyword_new[pos])) % len(ALPHA_CAPS)]
        else:
            plaintext += symbol
    return plaintext
