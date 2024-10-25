"""Module for Vigenere encryption"""


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

    plainlen = len(plaintext)
    keylen = len(keyword)

    if keylen < plainlen:
        keyword = keyword * (plainlen // keylen) + keyword[0 : plainlen % keylen]

    abclen = ord("Z") - ord("A") + 1

    for i, c in enumerate(plaintext):
        if c.isalpha() and keyword[i].isalpha():
            symbol = c.upper()
            key = keyword[i].upper()

            symbol = chr((ord(symbol) - ord("A") + ord(key) - ord("A")) % abclen + ord("A"))
            ciphertext += symbol if c.isupper() else symbol.lower()
        else:
            ciphertext += c

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

    ciplen = len(ciphertext)
    keylen = len(keyword)

    if keylen < ciplen:
        keyword = keyword * (ciplen // keylen) + keyword[0 : ciplen % keylen]

    abclen = ord("Z") - ord("A") + 1

    for i, c in enumerate(ciphertext):
        if c.isalpha() and keyword[i].isalpha():
            symbol = c.upper()
            key = keyword[i].upper()

            symbol = chr((ord(symbol) - ord("A") - (ord(key) - ord("A"))) % abclen + ord("A"))
            plaintext += symbol if c.isupper() else symbol.lower()
        else:
            plaintext += c

    return plaintext
