"""
Encrypting and decrypting a Caesar cipher
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
    for i in plaintext:
        if i.isalpha() is False:
            ciphertext += i
            continue
        if i.isupper() is True:
            if (ord(i) + shift) > 90:
                # print(chr((ord(i) + shift) % 90 + 64))
                ciphertext += chr((ord(i) + shift) % 90 + 64)
            else:
                # print(chr((ord(i) + shift) % 90), i, ord(i) + shift)
                ciphertext += chr(ord(i) + shift)
        else:
            if (ord(i) + shift) > 122:
                ciphertext += chr((ord(i) + shift) % 122 + 96)
            else:
                ciphertext += chr(ord(i) + shift)

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
    for i in ciphertext:
        if i.isalpha() is False:
            plaintext += i
            continue
        if i.isupper() is True:
            if (ord(i) - shift) < 65:
                # print(chr(90 - (shift - ord(i) + 64)))
                plaintext += chr(90 - (shift - ord(i) + 64))
            else:
                # print(chr(ord(i) - shift), i, ord(i) + shift)
                plaintext += chr(ord(i) - shift)
        else:
            if (ord(i) - shift) < 97:
                plaintext += chr(122 - (shift - ord(i) + 96))
            else:
                # print(chr((ord(i) + shift) % 90), i, ord(i) + shift)
                plaintext += chr(ord(i) - shift)

    return plaintext


# print(encrypt_caesar("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 15))
