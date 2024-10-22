"""
Atbash module
"""


def encrypt_atbash(plaintext: str):
    """
    Encrypts text intp Atbash cipher
    """
    ciphertext = ""
    for symbol in plaintext:
        if symbol.isalpha():
            gap = ord(symbol) - ord("a" if symbol.islower() else "A")
            ciphertext += chr(ord("z" if symbol.islower() else "Z") - gap)
        else:
            ciphertext += symbol

    return ciphertext
