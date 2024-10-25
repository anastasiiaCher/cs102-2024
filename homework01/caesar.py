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
    for element in plaintext:
        if element.isalpha() == False:
            ciphertext += element
        else:
            if element == element.upper():
                strt = ord("A")
            else:
                strt = ord("a")
            new_ascii_index = (ord(element) + shift - strt) % 26 + strt
            ciphertext += chr(new_ascii_index)
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
    for element in ciphertext:
        if element.isalpha() == False:
            plaintext += element
        else:
            if element == element.upper():
                strt = ord("A")
            else:
                strt = ord("a")
            new_ascii_index = (ord(element) - shift - strt) % 26 + strt
            plaintext += chr(new_ascii_index)
    return plaintext
