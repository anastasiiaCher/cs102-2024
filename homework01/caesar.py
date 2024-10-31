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
        if i.isalpha() and i.isupper():
            if ord(i) + shift > ord("Z"):
                ciphertext += chr(ord(i) + (shift - 26))
            else:
                ciphertext += chr(ord(i) + shift)
        elif i.isalpha() and i.islower():
            if ord(i) + shift > ord("z"):
                ciphertext += chr(ord(i) + (shift - 26))
            else:
                ciphertext += chr(ord(i) + shift)
        elif not (i.isalpha()):
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
        if i.isalpha() and i.isupper():
            if ord(i) - shift < ord("A"):
                plaintext += chr(ord(i) + (26 - shift))
            else:
                plaintext += chr(ord(i) - shift)
        elif i.isalpha() and i.islower():
            if ord(i) - shift < ord("a"):
                plaintext += chr(ord(i) + (26 - shift))
            else:
                plaintext += chr(ord(i) - shift)
        elif not (i.isalpha()):
            plaintext += i
    return plaintext
