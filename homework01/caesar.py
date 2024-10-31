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
    i = 0
    ciphertext = ""
    for i in range(len(plaintext)):
        sim = ord(plaintext[i])
        if sim < 65 or sim > 90 and sim < 97 or sim > 122:
            ciphertext = ciphertext + chr(sim)
        else:
            if sim <= 90 and (sim + shift) <= 90:
                ciphertext = ciphertext + chr(sim + shift)
            if sim <= 90 and (sim + shift) > 90:
                ciphertext = ciphertext + chr(65 + ((sim + shift) - 91))
            if sim >= 97 and (sim + shift) > 122:
                ciphertext = ciphertext + chr(97 + ((sim + shift) - 123))
            if sim >= 97 and (sim + shift) <= 122:
                ciphertext = ciphertext + chr(sim + shift)
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
    i = 0
    for i in range(len(ciphertext)):
        sim = ord(ciphertext[i])
        if sim < 65 or sim > 90 and sim < 97 or sim > 122:
            plaintext = plaintext + chr(sim)
        else:
            if sim <= 90 and (sim - shift) >= 65:
                plaintext = plaintext + chr(sim - (shift))
            if sim <= 90 and (sim - shift) < 65:
                plaintext = plaintext + chr(90 - (63 - (sim - shift - 1)))
            if sim >= 97 and (sim - shift) < 97:
                plaintext = plaintext + chr(122 - (95 - (sim - shift - 1)))
            if sim >= 97 and (sim - shift) >= 97:
                plaintext = plaintext + chr(sim - (shift))
    return plaintext
