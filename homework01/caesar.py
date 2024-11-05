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
            nbuk = ord(i) + shift
            if i.islower():
                if nbuk > ord("z"):
                    nbuk = nbuk - 26
            elif i.isupper():
                if nbuk > ord("Z"):
                    nbuk = nbuk - 26
            otv = chr(nbuk)
            ciphertext += otv
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
            nbuk = ord(i) - shift
            if i.islower():
                if nbuk < ord("a"):
                    nbuk = nbuk + 26
            elif i.isupper():
                if nbuk < ord("A"):
                    nbuk = nbuk + 26
            otv = chr(nbuk)
            plaintext += otv
        else:
            plaintext += i
    return plaintext
