"""
This module allows to encode and decipher strings using Ceaser cipher
"""


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for letter in plaintext:
        if "a" <= letter <= "z":
            ciphertext += chr(ord("a") + (ord(letter) - ord("a") + shift) % 26)
        elif "A" <= letter <= "Z":
            ciphertext += chr(ord("A") + (ord(letter) - ord("A") + shift) % 26)
        else:
            ciphertext += letter
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for letter in ciphertext:
        if "a" <= letter <= "z":
            plaintext += chr(ord("a") + (ord(letter) - ord("a") - shift) % 26)
        elif "A" <= letter <= "Z":
            plaintext += chr(ord("A") + (ord(letter) - ord("A") - shift) % 26)
        else:
            plaintext += letter
    return plaintext
