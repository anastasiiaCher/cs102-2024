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
    for char in plaintext:
        if char.isalpha():
            start = ord("a") if char.islower() else ord("A")
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
        else:
            shifted_char = char
        ciphertext += shifted_char
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
    for char in ciphertext:
        if char.isalpha():
            start = ord("a") if char.islower() else ord("A")
            shifted_char = chr((ord(char) - start - shift+26) % 26 + start)
        else:
            shifted_char = char
        plaintext += shifted_char
    return plaintext
