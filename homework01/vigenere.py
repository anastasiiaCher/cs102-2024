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
    keyword = keyword * ((len(plaintext) // len(keyword)) + 1)

    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(keyword[i].upper()) - ord("A")
            shifted_char = chr(((ord(char.upper()) + shift - ord("A")) % 26) + ord("A"))
            if char.islower():
                shifted_char = shifted_char.lower()
            ciphertext += shifted_char
        else:
            ciphertext += char
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
    keyword = keyword * ((len(ciphertext) // len(keyword)) + 1)

    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(keyword[i].upper()) - ord("A")
            shifted_char = chr(((ord(char.upper()) - shift - ord("A")) % 26) + ord("A"))
            if char.islower():
                shifted_char = shifted_char.lower()
            plaintext += shifted_char
        else:
            plaintext += char
    return plaintext
