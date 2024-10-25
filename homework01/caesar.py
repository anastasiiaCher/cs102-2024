"""Module for Caesar encryption"""


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
    for ch in plaintext:
        symbol = ""

        if "A" <= ch <= "Z":
            symbol = chr((ord(ch) - ord("A") + shift) % (ord("Z") - ord("A") + 1) + ord("A"))
        elif "a" <= ch <= "z":
            symbol = chr((ord(ch) - ord("a") + shift) % (ord("z") - ord("a") + 1) + ord("a"))
        else:
            symbol = ch
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
    for ch in ciphertext:
        symbol = ""

        if "A" <= ch <= "Z":
            symbol = chr((ord(ch) - ord("A") - shift) % (ord("Z") - ord("A") + 1) + ord("A"))
        elif "a" <= ch <= "z":
            symbol = chr((ord(ch) - ord("a") - shift) % (ord("z") - ord("a") + 1) + ord("a"))
        else:
            symbol = ch
        plaintext += symbol

    return plaintext
