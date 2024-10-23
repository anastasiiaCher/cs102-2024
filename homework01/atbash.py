"""
Encrypts and decrypts a text using Atbash cipher.
"""

def encrypt_atbash(plaintext: str) -> str:
    """
    Encrypts the given text.
    """
    ciphertext = ""
    for symbol in plaintext:
        if symbol.isalpha() and symbol.isupper():
            ciphertext += chr(ord("А") + ord("Я") - ord(symbol) - 1)
        elif symbol.isalpha() and symbol.islower():
            ciphertext += chr(ord("а") + ord("я") - ord(symbol) - 1)
        else:
            ciphertext += symbol
    return ciphertext
