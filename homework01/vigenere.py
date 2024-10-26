"""
This module provides functions for encrypting and decrypting messages using the Vigenere cipher.
"""


def letter_number(letter: str) -> int:
    if "A" <= letter <= "Z":
        return ord(letter) - ord("A")
    if "a" <= letter <= "z":
        return ord(letter) - ord("a")
    return -1


def number_to_letter(number: int, is_upper: bool) -> str:
    if is_upper:
        return chr(number + ord("A"))
    return chr(number + ord("a"))


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
    keyword_rep = (keyword * ((len(plaintext) // len(keyword)) + 1))[: len(plaintext)]

    for i, letter in enumerate(plaintext):
        key_letter = keyword_rep[i]
        num = letter_number(letter)
        key_num = letter_number(key_letter)

        if num != -1:
            shift = key_num
            is_upper = letter.isupper()
            shifted_num = (num + shift) % 26
            ciphertext += number_to_letter(shifted_num, is_upper)
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
    keyword_rep = (keyword * ((len(ciphertext) // len(keyword)) + 1))[: len(ciphertext)]

    for i, letter in enumerate(ciphertext):
        key_letter = keyword_rep[i]
        num = letter_number(letter)
        key_num = letter_number(key_letter)

        if num != -1:
            shift = key_num
            is_upper = letter.isupper()
            shifted_num = (num - shift) % 26
            plaintext += number_to_letter(shifted_num, is_upper)
        else:
            plaintext += letter
    return plaintext
