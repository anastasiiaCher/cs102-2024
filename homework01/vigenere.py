def encrypt_vigenere(plaintext: str, Schlusselwort: str) -> str:
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
    Schlusselwort = Schlusselwort * ((len(plaintext) // len(Schlusselwort)) + 1)
    indx = -1
    for i in plaintext:
        indx = indx + 1
        if i.isalpha() is False:
            ciphertext = ciphertext + i
            continue
        if i.isupper() is True:
            shift = (ord(Schlusselwort[indx]) - 65) % 26
            if (ord(i) + shift) > 90:
                ciphertext = ciphertext + chr(((ord(i) + shift) % 90) + 64)
            else:
                ciphertext = ciphertext + chr(ord(i) + shift)
        else:
            shift = (ord(Schlusselwort[indx]) - 97) % 26
            if (ord(i) + shift) > 122:
                ciphertext = ciphertext + chr(((ord(i) + shift) % 122) + 96)
            else:
                ciphertext = ciphertext + chr(ord(i) + shift)
    return ciphertext


def decrypt_vigenere(ciphertext: str, Schlusselwort: str) -> str:
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
    Schlusselwort = Schlusselwort * ((len(ciphertext) // len(Schlusselwort)) + 1)
    indx = -1
    for i in ciphertext:
        indx = indx + 1
        if i.isalpha() is False:
            plaintext += i
            continue
        if i.isupper() is True:
            shift = (ord(Schlusselwort[indx]) - 65) % 26
            if (ord(i) - shift) < 65:
                plaintext = plaintext + (chr(90 - (shift - ord(i) + 64)))
            else:
                plaintext = plaintext + (chr(ord(i) - shift))
        else:
            shift = (ord(Schlusselwort[indx]) - 97) % 26
            if (ord(i) - shift) < 97:
                plaintext = plaintext + (chr(122 - (shift - ord(i) + 96)))
            else:
                plaintext = plaintext + (chr(ord(i) - shift))
    return plaintext
