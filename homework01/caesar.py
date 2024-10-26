"""
This module provides functions to encrypt and decrypt text using a Caesar cipher.
"""


def letter_number(letter: str) -> int:
    """
    This function takes a letter and returns its position in the alphabet.
    """
    if "A" <= letter <= "Z":
        return ord(letter) - ord("A")
    if "a" <= letter <= "z":
        return ord(letter) - ord("a")
    return -1


def number_to_letter(number: int, is_upper: bool) -> str:
    """
    This function takes a number and returns the corresponding letter in the alphabet.
    """
    if is_upper:
        return chr(number + ord("A"))
    return chr(number + ord("a"))


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
        num = letter_number(letter)
        if num != -1:
            is_upper = letter.isupper()
            shifted_num = (num + shift) % 26
            ciphertext += number_to_letter(shifted_num, is_upper)
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
        num = letter_number(letter)
        if num != -1:
            is_upper = letter.isupper()
            shifted_num = (num - shift) % 26
            plaintext += number_to_letter(shifted_num, is_upper)
        else:
            plaintext += letter
    return plaintext
