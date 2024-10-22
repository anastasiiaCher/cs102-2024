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

    for a, alpha in zip(keyword, plaintext):
        if a.isalpha():
            shift = ord(a) - ord("A")
            if "A" <= alpha <= "Z":
                ciphertext += chr(ord("A") + ((ord(alpha) + shift - ord("A")) % 26))
            elif "a" <= alpha <= "z":
                ciphertext += chr(ord("a") + ((ord(alpha) + shift - ord("a")) % 26))
            else:
                ciphertext += alpha
        elif a.isnumeric() or a.isalnum() is False:
            if ord(alpha) - 1 < ord("A"):
                ciphertext += "Z"
            elif ord(alpha) - 1 < ord("a"):
                ciphertext += "z"
            else:
                ciphertext += chr(ord(alpha) - 1)
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

    for a, alpha in zip(keyword, ciphertext):
        if a.isalpha():
            shift = ord(a) - ord("A")
            if "A" <= alpha <= "Z":
                plaintext += chr(ord("Z") - ((ord("Z") - ord(alpha) + shift) % 26))
            elif "a" <= alpha <= "z":
                plaintext += chr(ord("z") - ((ord("z") - ord(alpha) + shift) % 26))
            else:
                plaintext += alpha
        elif a.isnumeric() or a.isalnum() is False:
            if ord(alpha) + 1 < ord("A"):
                plaintext += "Z"
            elif ord(alpha) + 1 < ord("a"):
                plaintext += "z"
            else:
                plaintext += chr(ord(alpha) + 1)
    return plaintext
