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
    key = (keyword * (len(plaintext) // len(keyword))) + keyword[: len(plaintext) % len(keyword)]
    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = 0
            if key[i].islower():
                shift = ord(key[i]) - 97
            elif key[i].isupper():
                shift = ord(key[i]) - 65
            char_code = ord(char) + shift
            if char.islower() and char_code > ord("z"):
                char_code = char_code - 26
            elif char.isupper() and char_code > ord("Z"):
                char_code = char_code - 26
            otv = chr(char_code)
            ciphertext += otv
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
    key = (keyword * (len(ciphertext) // len(keyword))) + keyword[: len(ciphertext) % len(keyword)]
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = 0
            if key[i].islower():
                shift = ord(key[i]) - 97
            elif key[i].isupper():
                shift = ord(key[i]) - 65
            char_code = ord(char) - shift
            if char.islower() and char_code < ord("a"):
                char_code = char_code + 26
            elif char.isupper() and char_code < ord("A"):
                char_code = char_code + 26
            otv = chr(char_code)
            plaintext += otv
        else:
            plaintext += char
    return plaintext
