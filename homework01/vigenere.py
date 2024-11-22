"""Vigenere cipher machine"""


def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """Encrypting with Vigenere cipher"""
    ciphertext = ""
    key = keyword * (len(plaintext) // len(keyword)) + keyword[: (len(plaintext) % len(keyword))]
    for i in enumerate(plaintext):
        let = plaintext[i[0]]
        if let.islower():
            shift = ord(key[i[0]]) - ord("a")
            ciphertext += chr((ord(let) + shift - ord("a")) % 26 + ord("a"))
        elif let.isupper():
            shift = ord(key[i[0]]) - ord("A")
            ciphertext += chr((ord(let) + shift - ord("A")) % 26 + ord("A"))
        else:
            ciphertext += let
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """Decrypting with Vigenere cipher"""
    plaintext = ""
    key = keyword * (len(ciphertext) // len(keyword)) + keyword[: (len(ciphertext) % len(keyword))]
    for i in enumerate(ciphertext):
        let = ciphertext[i[0]]
        if let.islower():
            shift = ord(key[i[0]]) - ord("a")
            plaintext += chr((ord(let) - shift - ord("a")) % 26 + ord("a"))
        elif let.isupper():
            shift = ord(key[i[0]]) - ord("A")
            plaintext += chr((ord(let) - shift - ord("A")) % 26 + ord("A"))
        else:
            plaintext += let
    return plaintext
