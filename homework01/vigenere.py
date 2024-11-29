def encrypt_vigenere(plaintext, keyword):
    """
    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """

    ciphertext = ""
    key_repeated = (keyword * (len(plaintext) // len(keyword))) + keyword[: len(plaintext) % len(keyword)]
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = ord(key_repeated[i].upper()) - ord("A")
            if plaintext[i].isupper():
                ciphertext += chr((ord(plaintext[i]) + shift - ord("A")) % 26 + ord("A"))
            else:
                ciphertext += chr((ord(plaintext[i]) + shift - ord("a")) % 26 + ord("a"))
        else:
            ciphertext += plaintext[i]
    return ciphertext


def decrypt_vigenere(ciphertext, keyword):
    """
    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    key_repeated = (keyword * (len(ciphertext) // len(keyword))) + keyword[: len(ciphertext) % len(keyword)]
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = ord(key_repeated[i].upper()) - ord("A")
            if ciphertext[i].isupper():
                plaintext += chr((ord(ciphertext[i]) - shift - ord("A")) % 26 + ord("A"))
            else:
                plaintext += chr((ord(ciphertext[i]) - shift - ord("a")) % 26 + ord("a"))
        else:
            plaintext += ciphertext[i]
    return plaintext
