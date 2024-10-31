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
    # PUT YOUR CODE HERE
    keyword_repeated = (keyword * ((len(plaintext) // len(keyword)) + 1))[
        : len(plaintext)
    ]
    for p, k in zip(plaintext, keyword_repeated):
        if p.isupper():
            shift = ord(k.upper()) - ord("A")
            cipher_char = chr((ord(p) - ord("A") + shift) % 26 + ord("A"))
        elif p.islower():
            shift = ord(k.lower()) - ord("a")
            cipher_char = chr((ord(p) - ord("a") + shift) % 26 + ord("a"))
        else:
            cipher_char = p
        ciphertext += cipher_char
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
    # PUT YOUR CODE HERE
    keyword_repeated = (keyword * ((len(ciphertext) // len(keyword)) + 1))[
        : len(ciphertext)
    ]
    for c, k in zip(ciphertext, keyword_repeated):
        if c.isupper():
            shift = ord(k.upper()) - ord("A")
            plain_char = chr((ord(c) - ord("A") - shift + 26) % 26 + ord("A"))
        elif c.islower():
            shift = ord(k.lower()) - ord("a")
            plain_char = chr((ord(c) - ord("a") - shift + 26) % 26 + ord("a"))
        else:
            plain_char = c
        plaintext += plain_char
    return plaintext
