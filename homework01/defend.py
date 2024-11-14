"""
Encryption problem to defend the 1 lab.
"""


def encrypt_affine(plaintext, a, b):
    """
    Affine sencrypt algorithm.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    ALPHABET = alphabet.upper()

    ciphertext = ""
    for letter in plaintext:
        if letter in alphabet:
            x = alphabet.index(letter)
            ciphertext += alphabet[(a * x + b) % 26]
        elif letter in ALPHABET:
            x = ALPHABET.index(letter)
            ciphertext += ALPHABET[(a * x + b) % 26]
        else:
            ciphertext += letter

    return ciphertext
