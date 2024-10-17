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
    for alpha in plaintext:
        if ord("A") <= ord(alpha) <= ord("Z"):
            if (ord(alpha) + shift) - ord("A") > 25:
                alpha = chr(ord(alpha) + shift - 26)
                ciphertext += alpha
            else:
                alpha = chr(ord(alpha) + shift)
                ciphertext += alpha
        elif ord("a") <= ord(alpha) <= ord("z"):
            if (ord(alpha) + shift) - ord("a") > 25:
                alpha = chr(ord(alpha) + shift - 26)
                ciphertext += alpha
            else:
                alpha = chr(ord(alpha) + shift)
                ciphertext += alpha

        else:
            ciphertext += alpha
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
    for alpha in ciphertext:
        if ord("A") <= ord(alpha) <= ord("Z"):
            if ord("Z") - (ord(alpha) - shift) > 25:
                alpha = chr(ord(alpha) - shift + 26)
                plaintext += alpha
            else:
                alpha = chr(ord(alpha) - shift)
                plaintext += alpha
        elif ord("a") <= ord(alpha) <= ord("z"):
            if ord("z") - (ord(alpha) - shift) > 25:
                alpha = chr(ord(alpha) - shift + 26)
                plaintext += alpha
            else:
                alpha = chr(ord(alpha) - shift)
                plaintext += alpha

        else:
            plaintext += alpha
    return plaintext
