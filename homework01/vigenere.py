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
    ciphertext = []
    for i in range(len(plaintext)):
        if i > len(keyword) - 1:
            if ord(keyword[i % len(keyword)]) >= 65 and ord(keyword[i % len(keyword)]) <= 90:
                shift = ord(keyword[i % len(keyword)]) - ord("A")
            else:
                shift = ord(keyword[i % len(keyword)]) - ord("a")
        else:
            if ord(keyword[i]) >= 65 and ord(keyword[i]) <= 90:
                shift = ord(keyword[i]) - ord("A")
            else:
                shift = ord(keyword[i]) - ord("a")

        if ord(plaintext[i]) >= 65 and ord(plaintext[i]) <= 90:
            b = chr(ord(plaintext[i]) + shift)
            if ord(b) > 90:
                b = chr(ord(b) - 26)
            ciphertext.append(b)
        elif ord(plaintext[i]) >= 97 and ord(plaintext[i]) <= 122:
            b = chr(ord(plaintext[i]) + shift)
            if ord(b) > 122:
                b = chr(ord(b) - 26)
            ciphertext.append(b)
        else:
            ciphertext.append(plaintext[i])
    return "".join([str(i) for i in ciphertext])


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
    plaintext = []
    for i in range(len(ciphertext)):
        if i > len(keyword) - 1:
            if ord(keyword[i % len(keyword)]) >= 65 and ord(keyword[i % len(keyword)]) <= 90:
                shift = ord(keyword[i % len(keyword)]) - ord("A")
            else:
                shift = ord(keyword[i % len(keyword)]) - ord("a")
        else:
            if ord(keyword[i]) >= 65 and ord(keyword[i]) <= 90:
                shift = ord(keyword[i]) - ord("A")
            else:
                shift = ord(keyword[i]) - ord("a")

        if ord(ciphertext[i]) >= 65 and ord(ciphertext[i]) <= 90:
            b = chr(ord(ciphertext[i]) - shift)
            if ord(b) < 65:
                b = chr(ord(b) + 26)
            plaintext.append(b)
        elif ord(ciphertext[i]) >= 97 and ord(ciphertext[i]) <= 122:
            b = chr(ord(ciphertext[i]) - shift)
            if ord(b) < 97:
                b = chr(ord(b) + 26)
            plaintext.append(b)
        else:
            plaintext.append(ciphertext[i])
    return "".join([str(i) for i in plaintext])
