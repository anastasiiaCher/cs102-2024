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
    key_length = len(keyword)
    key_as_int = [ord(i) for i in keyword]
    plaintext_int = [ord(i) for i in plaintext]

    for i in range(len(plaintext_int)):
        key_index = i % key_length
        shift = key_as_int[key_index]

        if plaintext[i].islower():
            value = (plaintext_int[i] - ord("a") + shift - ord("a")) % 26 + ord("a")
            ciphertext += chr(value)
        elif plaintext[i].isupper():
            value = (plaintext_int[i] - ord("A") + shift - ord("A")) % 26 + ord("A")
            ciphertext += chr(value)
        else:
            ciphertext += plaintext[i]

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
    key_length = len(keyword)
    key_as_int = [ord(i) for i in keyword]
    ciphertext_int = [ord(i) for i in ciphertext]

    for i in range(len(ciphertext_int)):
        key_index = i % key_length
        shift = key_as_int[key_index]

        if ciphertext[i].islower():
            value = (ciphertext_int[i] - shift) % 26 + ord("a")
            plaintext += chr(value)
        elif ciphertext[i].isupper():
            value = (ciphertext_int[i] - ord("A") - shift - ord("A")) % 26 + ord("A")
            plaintext += chr(value)
        else:
            plaintext += ciphertext[i]
    return plaintext
