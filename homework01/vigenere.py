"""
This module allows one to encrypt and decrypt messages using Viginaire cipher
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
    lock = zip(plaintext, keyword * len(plaintext))
    for letter, key in lock:
        if "a" <= letter <= "z":
            ciphertext += chr(ord("a") + (ord(letter) - 2 * ord("a") + ord(key.lower())) % 26)
        elif "A" <= letter <= "Z":
            ciphertext += chr(ord("A") + (ord(letter) - 2 * ord("A") + ord(key.upper())) % 26)
        else:
            ciphertext += letter
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
    lock = zip(ciphertext, keyword * len(ciphertext))
    for letter, key in lock:
        if "a" <= letter <= "z":
            plaintext += chr(ord("a") + (ord(letter) - ord(key.lower())) % 26)
        elif "A" <= letter <= "Z":
            plaintext += chr(ord("A") + (ord(letter) - ord(key.upper())) % 26)
        else:
            plaintext += letter
    return plaintext
