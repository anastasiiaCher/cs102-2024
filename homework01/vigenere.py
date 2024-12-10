"""Алгоритм позволяет зашифровать и расшифровать сообщение при помощи шифра Виженера."""

ALPHA = "abcdefghijklmnopqrstuvwxyz"
ALPHA_CAPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


ALPHA = "abcdefghijklmnopqrstuvwxyz"
ALPHA_CAPS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


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
    keyword_new = keyword * (len(plaintext) // len(keyword))
    keyword_new += keyword[: (len(plaintext) % len(keyword))]

    for i in range(len(plaintext)):
        s = plaintext[i]
        if s in ALPHA:
            ciphertext += ALPHA[(ALPHA.find(s) + ALPHA.find(keyword_new[i])) % len(ALPHA)]
        elif s in ALPHA_CAPS:
            ciphertext += ALPHA_CAPS[(ALPHA_CAPS.find(s) + ALPHA_CAPS.find(keyword_new[i])) % len(ALPHA_CAPS)]
        else:
            ciphertext += s
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
    keyword_new = keyword * (len(ciphertext) // len(keyword))
    keyword_new += keyword[: (len(ciphertext) % len(keyword))]

    for i in range(len(ciphertext)):
        s = ciphertext[i]
        if s in ALPHA:
            plaintext += ALPHA[(ALPHA.find(s) - ALPHA.find(keyword_new[i])) % len(ALPHA)]
        elif s in ALPHA_CAPS:
            plaintext += ALPHA_CAPS[(ALPHA_CAPS.find(s) - ALPHA_CAPS.find(keyword_new[i])) % len(ALPHA_CAPS)]
        else:
            plaintext += s
    return plaintext


# print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))
# print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))
