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
            kod = ord(i)
            if (ord("Z") - shift + 1) <= kod <= ord("Z") and shift > 0:
                ciphertext += chr(kod - 26 + shift)
            elif kod >= (ord("z") - shift + 1) and shift > 0:
                ciphertext += chr(kod - 26 + shift)
            else:
                ciphertext += chr(kod + shift)
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
            kod = ord(i)
            if ord("A") <= kod <= (ord("A") + shift - 1) and shift > 0:
                plaintext += chr(kod + 26 - shift)
            elif ord("a") <= kod <= (ord("a") + shift - 1) and shift > 0:
                plaintext += chr(kod + 26 - shift)
            else:
                plaintext += chr(kod - shift)
        else:
            plaintext += i
    return plaintext
