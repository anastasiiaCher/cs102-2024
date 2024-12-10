"""
The module allows you to encrypt messages via affine cypher
"""


def encrypt_affine(plaintext: str, a: int = 1, b: int = 3) -> str:
    """
    this is the cypher most ancient
    """
    ciphertext = ""
    for letter in plaintext:
        if "a" <= letter <= "z":
            ciphertext += chr(ord("a") + ((ord(letter) - ord("a")) * a + b) % 26)
        elif "A" <= letter <= "Z":
            ciphertext += chr(ord("A") + ((ord(letter) - ord("A")) * a + b) % 26)
        else:
            ciphertext += letter
    return ciphertext
