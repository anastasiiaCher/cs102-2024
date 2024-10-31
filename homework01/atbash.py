"""
    Atbash encrypter
"""


def encrypt_atbash(plaintext: str) -> str:
    """
    Encrypts plaintext using a Atbash cipher.
    """

    ciphertext = ""
    for i in range(len(plaintext)):
        char_code = plaintext[i]
        if char_code.islower():
            ciphertext += chr(ord("a") + (26 - ((ord(char_code) - ord("a")) % 26 + 1)))
        elif char_code.isupper():
            ciphertext += chr(ord("A") + (26 - ((ord(char_code) - ord("A")) % 26 + 1)))
        else:
            ciphertext += char_code

    return ciphertext


print(encrypt_atbash("abcdef"))
