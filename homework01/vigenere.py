def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    key = (keyword * (len(plaintext) // len(keyword))) + keyword[: len(plaintext) % len(keyword)]
    for i, val in enumerate(plaintext):
        if val.isalpha():
            shift = 0
            if key[i].islower():
                shift = ord(key[i]) - 97
            elif key[i].isupper():
                shift = ord(key[i]) - 65
            nbuk = ord(val) + shift
            if val.islower() and nbuk > ord("z"):
                nbuk = nbuk - 26
            elif val.isupper() and nbuk > ord("Z"):
                nbuk = nbuk - 26
            otv = chr(nbuk)
            ciphertext += otv
        else:
            ciphertext += val

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    key = (keyword * (len(ciphertext) // len(keyword))) + keyword[: len(ciphertext) % len(keyword)]
    for i, val in enumerate(ciphertext):
        if val.isalpha():
            shift = 0
            if key[i].islower():
                shift = ord(key[i]) - 97
            elif key[i].isupper():
                shift = ord(key[i]) - 65
            nbuk = ord(val) - shift
            if val.islower() and nbuk < ord("a"):
                nbuk = nbuk + 26
            elif val.isupper() and nbuk < ord("A"):
                nbuk = nbuk + 26
            otv = chr(nbuk)
            plaintext += otv
        else:
            plaintext += val
    return plaintext
