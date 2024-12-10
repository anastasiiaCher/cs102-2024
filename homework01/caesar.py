"""Алгоритм позволяет зашифровать и расшифровать сообщение при помощи шифра Цезаря."""

alpha = "abcdefghijklmnopqrstuvwxyz"
alpha_caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


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
    for pos, symbol in enumerate(plaintext):
        if symbol in alpha:
            ciphertext += alpha[(alpha.index(symbol) + shift) % len(alpha)]
        elif symbol in alpha_caps:
            ciphertext += alpha_caps[(alpha_caps.index(symbol) + shift) % len(alpha_caps)]
        else:
            ciphertext += symbol
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
    for pos, symbol in enumerate(ciphertext):
        if symbol in alpha:
            plaintext += alpha[(alpha.index(symbol) - shift) % len(alpha)]
        elif symbol in alpha_caps:
            plaintext += alpha_caps[(alpha_caps.index(symbol) - shift) % len(alpha_caps)]
        else:
            plaintext += symbol
    return plaintext
