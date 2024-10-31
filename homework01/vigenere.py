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
    key = (keyword * ((len(plaintext) // len(keyword)) + 1))[: len(plaintext)]
    for i, key_i in zip(plaintext, key):
        if i.isalpha():
            shift = ord(key_i.upper()) - ord("A")
            fund = ord("A") if i.isupper() else ord("a")
            then_i = chr((ord(i) - fund + shift) % 26 + fund)
            ciphertext += then_i
        else:
            ciphertext += i
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
    key = (keyword * ((len(ciphertext) // len(keyword)) + 1))[: len(ciphertext)]
    for i, key_i in zip(ciphertext, key):
        if i.isalpha():
            shift = ord(key_i.upper()) - ord("A")
            fund = ord("A") if i.isupper() else ord("a")
            then_i = chr((ord(i) - fund - shift) % 26 + fund)
            plaintext += then_i
        else:
            plaintext += i
    return plaintext
