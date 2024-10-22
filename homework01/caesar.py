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

    for sym in plaintext:
        if sym.isalpha():
            if sym.isupper():
                first = ord('A')
            else:
                first = ord('a')
            after = (ord(sym) - first + shift) % 26 + first
            ciphertext += chr(after)
        else:
            ciphertext += sym

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
    for sym in ciphertext:
        if sym.isalpha():
            if sym.isupper():
                first = ord('A')
            else:
                first = ord('a')
            after = (ord(sym) - first - shift) % 26 + first
            plaintext += chr(after)
        else:
            plaintext += sym
    return plaintext
