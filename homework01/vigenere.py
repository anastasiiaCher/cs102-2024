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
    keyword = (keyword * ((len(plaintext) // len(keyword)) + 1))[: len(plaintext)]
    for p, k in zip(plaintext, keyword):
        if p.isalpha():
            shift = ord(k.upper()) - ord("A")
            if p.islower():
                ciphertext += chr((ord(p) - ord("a") + shift) % 26 + ord("a"))
            elif p.isupper():
                ciphertext += chr((ord(p) - ord("A") + shift) % 26 + ord("A"))
        else:
            ciphertext += p

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
    keyword = (keyword * ((len(ciphertext) // len(keyword)) + 1))[: len(ciphertext)]
    for c, k in zip(ciphertext, keyword):
        if c.isalpha():
            shift = ord(k.upper()) - ord("A")
            if c.islower():
                plaintext += chr((ord(c) - ord("a") - shift) % 26 + ord("a"))
            elif c.isupper():
                plaintext += chr((ord(c) - ord("A") - shift) % 26 + ord("A"))
        else:
            plaintext += c
    return plaintext
