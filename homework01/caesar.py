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
        if ord("a") > ord(i.lower()) or ord(i.lower()) > ord("z"):
            ciphertext += i
        if ord(i.lower()) + shift <= ord("z"):
            if i.isupper():
                ciphertext += (chr(ord(i.lower()) + shift)).upper()
            if i.islower():
                ciphertext += (chr(ord(i) + shift)).lower()
        else:
            if i.isupper():
                ciphertext += (chr(ord("a") + (ord(i.lower()) + shift - ord("z")) - 1)).upper()
            if i.islower():
                ciphertext += (chr(ord("a") + (ord(i) + shift - ord("z")) - 1)).lower()
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
        if ord("a") > ord(i.lower()) or ord(i.lower()) > ord("z"):
            plaintext += i
        if ord(i.lower()) - shift >= ord("a"):
            if i.isupper():
                plaintext += (chr(ord(i) - shift)).upper()
            if i.islower():
                plaintext += (chr(ord(i) - shift)).lower()
        else:
            if i.isupper():
                plaintext += (chr(ord(i) - ord("a") + ord("z") - shift + 1)).upper()
            if i.islower():
                plaintext += (chr(ord(i) - ord("a") + ord("z") - shift + 1)).lower()
    return plaintext
