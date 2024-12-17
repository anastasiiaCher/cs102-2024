import typing as tp


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
    ciphertext = []
    for i in range(len(plaintext)):
        if ord(plaintext[i]) >= 65 and ord(plaintext[i]) <= 90:
            b = chr(ord(plaintext[i]) + shift % 28)
            if ord(b) > 90:
                b = chr(ord(b) - 26)
            ciphertext.append(b)
        elif ord(plaintext[i]) >= 97 and ord(plaintext[i]) <= 122:
            b = chr(ord(plaintext[i]) + shift % 28)
            if ord(b) > 122:
                b = chr(ord(b) - 26)
            ciphertext.append(b)
        else:
            ciphertext.append(plaintext[i])
    return "".join([str(i) for i in ciphertext])


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
    plaintext = []
    for i in range(len(ciphertext)):
        if ord(ciphertext[i]) >= 65 and ord(ciphertext[i]) <= 90:
            b = chr(ord(ciphertext[i]) - shift % 28)
            if ord(b) < 65:
                b = chr(ord(b) + 26)
            plaintext.append(b)
        elif ord(ciphertext[i]) >= 97 and ord(ciphertext[i]) <= 122:
            b = chr(ord(ciphertext[i]) - shift % 28)
            if ord(b) < 97:
                b = chr(ord(b) + 26)
            plaintext.append(b)
        else:
            plaintext.append(ciphertext[i])
    return "".join([str(i) for i in plaintext])
