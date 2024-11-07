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

    for el in plaintext:
        if el.isupper():
            ord_letter = ord(el) + shift
            while ord_letter > ord('Z'):
                ord_letter -= 26
            ciphertext += chr(ord_letter)
        elif el.islower():
            ord_letter = ord(el) + shift
            while ord_letter > ord('z'):
                ord_letter -= 26
            ciphertext += chr(ord_letter)
        else:
            ciphertext += el
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

    for el in ciphertext:
        if el.isupper():
            ord_letter = ord(el) - shift
            while ord_letter < ord('A'):
                ord_letter += 26
            plaintext += chr(ord_letter)

        elif el.islower():
            ord_letter = ord(el) - shift
            while ord_letter < ord('a'):
                ord_letter += 26
            plaintext += chr(ord_letter)

        else:
            plaintext += el
    return plaintext
