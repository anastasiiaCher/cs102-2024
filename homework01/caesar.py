"""
Encrypts and decrypts a text using Caesar cipher and given shift.
"""


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
    shift %= 26
    for symbol in plaintext:
        if symbol.isalpha() and symbol.isupper():
            ciphertext += (
                chr(ord(symbol) + shift)
                if ord(symbol) + shift < 91
                else chr(ord(symbol) + shift - 26)
            )
        elif symbol.isalpha() and symbol.islower():
            ciphertext += (
                chr(ord(symbol) + shift)
                if ord(symbol) + shift < 123
                else chr(ord(symbol) + shift - 26)
            )
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
    shift %= 26
    for symbol in ciphertext:
        if symbol.isalpha() and symbol.isupper():
            plaintext += (
                chr(ord(symbol) - shift)
                if ord(symbol) - shift > 64
                else chr(ord(symbol) - shift + 26)
            )
        elif symbol.isalpha() and symbol.islower():
            plaintext += (
                chr(ord(symbol) - shift)
                if ord(symbol) - shift > 96
                else chr(ord(symbol) - shift + 26)
            )
        else:
            plaintext += symbol
    return plaintext
