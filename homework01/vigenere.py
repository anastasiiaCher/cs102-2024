from math import ceil


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

    keyword = (keyword * ceil(len(plaintext) / len(keyword)))[: len(plaintext)]  # ABCABCABC

    for a, b in zip(plaintext, keyword):
        if a.isalpha() and b.isalpha():
            shift = ord(b.lower()) - ord("a")

            if ord(a) + shift > ord("Z" if a.isupper() else "z"):
                a = chr(ord(a) + shift - 26)
            else:
                a = chr(ord(a) + shift)

        ciphertext += a
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

    keyword = (keyword * ceil(len(ciphertext) / len(keyword)))[: len(ciphertext)]

    for a, b in zip(ciphertext, keyword):
        if a.isalpha() and b.isalpha():
            shift = ord(b.lower()) - ord("a")

            if ord(a) - shift < ord("A" if a.isupper() else "a"):
                a = chr(ord(a) - shift + 26)
            else:
                a = chr(ord(a) - shift)

        plaintext += a
    return plaintext
