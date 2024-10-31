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
            numb = ord(i) + shift
            if i.islower():
                if numb > ord("z"):
                    numb = numb - 26
            elif i.isupper():
                if numb > ord("Z"):
                    numb = numb - 26
            ans = chr(numb)
            ciphertext += ans
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
            numb = ord(i) - shift
            if i.islower():
                if numb < ord("a"):
                    numb = numb + 26
            elif i.isupper():
                if numb < ord("A"):
                    numb = numb + 26
            ans = chr(numb)
            plaintext += ans
        else:
            plaintext += i
    return plaintext
