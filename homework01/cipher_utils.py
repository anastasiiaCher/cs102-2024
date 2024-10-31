"""
This module provides utility functions for cipher operations.
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


def process_text(text: str, shifts: list[int], encrypt: bool = True) -> str:
    """
    Processes the text for encryption or decryption using the provided shifts.
    """
    result = ""
    for i, letter in enumerate(text):
        num = letter_number(letter)
        if num != -1:
            shift = shifts[i % len(shifts)]
            if not encrypt:
                shift = -shift
            is_upper = letter.isupper()
            shifted_num = (num + shift) % 26
            result += number_to_letter(shifted_num, is_upper)
        else:
            result += letter
    return result
