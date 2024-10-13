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

    if len(keyword) == 1:
        dif = len(plaintext) - len(keyword)
        keyword += keyword * dif
    else:
        i = len(plaintext) // len(keyword)
        m = len(plaintext) % len(keyword)
        keyword += keyword * (i - 1) + keyword[:m]

    keyword = keyword.upper()

    for a, b in zip(keyword, plaintext):
        if ord(b) == ord(" "):
            ciphertext += b
        else:
            if a.isalpha():
                shift = ord(a) - ord("A")
                if ord("A") <= ord(b) <= ord("Z"):
                    if (ord(b) + shift) - ord("A") > 25:
                        ciphertext += chr(ord("A") + ord(b) + shift - ord("A") - 26)
                    else:
                        ciphertext += chr(ord(b) + shift)
                elif ord("a") <= ord(b) <= ord("z"):
                    if (ord(b) + shift) - ord("a") > 25:
                        ciphertext += chr(ord("a") + ord(b) + shift - ord("a") - 26)
                    else:
                        ciphertext += chr(ord(b) + shift)
            elif a.isnumeric() or a.isalnum() is False:
                if ord(b) - 1 < ord("A"):
                    ciphertext += "Z"
                elif ord(b) - 1 < ord("a"):
                    ciphertext += "z"
                else:
                    ciphertext += chr(ord(b) - 1)
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

    if len(keyword) == 1:
        dif = len(ciphertext) - len(keyword)
        keyword += keyword * dif
    else:
        i = len(ciphertext) // len(keyword)
        m = len(ciphertext) % len(keyword)
        keyword += keyword * (i - 1) + keyword[:m]

    keyword = keyword.upper()

    for a, b in zip(keyword, ciphertext):
        if ord(b) == ord(" "):
            plaintext += b
        else:
            if a.isalpha():
                shift = ord(a) - ord("A")
                if ord("A") <= ord(b) <= ord("Z"):
                    if ord("Z") - (ord(b) - shift) > 25:
                        plaintext += chr(ord("Z") - (ord("Z") - (ord(b) - shift) - 26))
                    else:
                        plaintext += chr(ord(b) - shift)
                elif ord("a") <= ord(b) <= ord("z"):
                    if ord("z") - (ord(b) - shift) > 25:
                        plaintext += chr(ord("z") - (ord("z") - (ord(b) - shift) - 26))
                    else:
                        plaintext += chr(ord(b) - shift)
            elif a.isnumeric() or a.isalnum() is False:
                if ord(b) + 1 < ord("A"):
                    plaintext += "Z"
                elif ord(b) + 1 < ord("a"):
                    plaintext += "z"
                else:
                    plaintext += chr(ord(b) + 1)
    return plaintext
