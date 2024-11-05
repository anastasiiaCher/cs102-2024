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
    for char in plaintext:
        if "a" <= char <= "z":
            ciphertext += chr(ord("a") + (ord(char) - ord("a") + shift) % 26)
        elif "A" <= char <= "Z":
            ciphertext += chr(ord("A") + (ord(char) - ord("A") + shift) % 26)
        else:
            ciphertext += char
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
    for char in ciphertext:
        if "a" <= char <= "z":
            plaintext += chr(ord("a") + (ord(char) - ord("a") - shift) % 26)
        elif "A" <= char <= "Z":
            plaintext += chr(ord("A") + (ord(char) - ord("A") - shift) % 26)
        else:
            plaintext += char
    return plaintext
