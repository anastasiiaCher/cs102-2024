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
    keyword_repeated = (keyword * (len(plaintext) // len(keyword) + 1))[: len(plaintext)]

    for p_char, k_char in zip(plaintext, keyword_repeated):
        if p_char.isalpha():
            shift = (ord(k_char.upper()) - ord("A")) % 26
            if p_char.isupper():
                new_char = chr((ord(p_char) - ord("A") + shift) % 26 + ord("A"))
            else:
                new_char = chr((ord(p_char) - ord("a") + shift) % 26 + ord("a"))
            ciphertext += new_char
        else:
            ciphertext += p_char

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
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword) + 1))[: len(ciphertext)]

    for c_char, k_char in zip(ciphertext, keyword_repeated):
        if c_char.isalpha():
            shift = (ord(k_char.upper()) - ord("A")) % 26
            if c_char.isupper():
                new_char = chr((ord(c_char) - ord("A") - shift) % 26 + ord("A"))
            else:
                new_char = chr((ord(c_char) - ord("a") - shift) % 26 + ord("a"))
            plaintext += new_char
        else:
            plaintext += c_char

    return plaintext
