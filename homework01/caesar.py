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
    for i in range(len(plaintext)):
        s = plaintext[i]
        if s in alpha:
            ciphertext += alpha[(alpha.index(s) + shift) % len(alpha)]
        elif s in alpha_caps:
            ciphertext += alpha_caps[(alpha_caps.index(s) + shift) % len(alpha_caps)]
        else:
            ciphertext += s
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
    for i in range(len(ciphertext)):
        s = ciphertext[i]
        if s in alpha:
            plaintext += alpha[(alpha.index(s) - shift) % len(alpha)]
        elif s in alpha_caps:
            plaintext += alpha_caps[(alpha_caps.index(s) - shift) % len(alpha_caps)]
        else:
            plaintext += s
    return plaintext


# print(encrypt_caesar("Python3.6"))
# print(decrypt_caesar("sbwkrq"))
