"""
    Homework01 extra task
"""


def encrypt_atbash(plaintext: str) -> str:
    """
    Encrypts plaintext using a AtBash cipher.
    """

    ciphertext = ""
    for i in range(len(plaintext)):
        letter = plaintext[i]
        if letter.islower():
            ciphertext += chr(ord("a") + (26 - ((ord(letter) - ord("a")) % 26 + 1)))
        elif letter.isupper():
            ciphertext += chr(ord("A") + (26 - ((ord(letter) - ord("A")) % 26 + 1)))
        else:
            ciphertext += letter

    return ciphertext
