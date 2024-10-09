"""
Module executing the Caesar cipher
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
    for i in plaintext:
        if i.isalpha():
            if i.isupper():
                temp = chr(65 + (((ord(i) - 13) % 26 + shift) % 26))
            else:
                temp = chr(97 + (((ord(i) - 19) % 26 + shift) % 26))
            ciphertext += temp
        else:
            ciphertext += i
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
    for i in ciphertext:
        if i.isalpha():
            if i.isupper():
                temp = chr(65 + (((ord(i) - 13) % 26 - shift) % 26))
            else:
                temp = chr(97 + (((ord(i) - 19) % 26 - shift) % 26))
            plaintext += temp
        else:
            plaintext += i
    return plaintext
