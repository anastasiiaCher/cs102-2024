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
    key_index = 0
    keyword_length = len(keyword)

    for letter in plaintext:
        if letter.isalpha():  # Only consider alphabetic characters
            key_char = keyword[key_index % keyword_length].upper()
            shift = ord(key_char) - ord("A")
            if letter.islower():
                ciphertext += chr((ord(letter) + shift - ord('a')) % 26 + ord('a'))
            elif letter.isupper():
                ciphertext += chr((ord(letter) + shift - ord('A')) % 26 + ord('A'))
            key_index += 1
        else:
            ciphertext += letter

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
    key_index = 0
    keyword_length = len(keyword)

    for letter in ciphertext:
        if letter.isalpha():  # Only consider alphabetic characters
            key_char = keyword[key_index % keyword_length].upper()
            shift = ord(key_char) - ord("A")
            if letter.islower():
                plaintext += chr((ord(letter) - shift - ord('a')) % 26 + ord('a'))
            elif letter.isupper():
                plaintext += chr((ord(letter) - shift - ord('A')) % 26 + ord('A'))
            key_index += 1
        else:
            plaintext += letter

    return plaintext
