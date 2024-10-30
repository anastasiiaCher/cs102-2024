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
    key = []
    key_index = 0

    for letter in plaintext:
        if letter.isalpha():  # Only consider alphabetic characters
            key.append(keyword[key_index % len(keyword)].upper())
            key_index += 1
        else:
            key.append(letter)

    for i in range(len(plaintext)):
        letter = plaintext[i]
        if letter.islower():
            shift = ord(key[i]) - ord("A")
            ciphertext += chr(((ord(letter) + shift - ord("a")) % 26 + ord("a")))
        elif letter.isupper():
            shift = ord(key[i]) - ord("A")
            ciphertext += chr(((ord(letter) + shift - ord("A")) % 26 + ord("A")))
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
    key = []
    key_index = 0

    for letter in ciphertext:
        if letter.isalpha():  # Only consider alphabetic characters
            key.append(keyword[key_index % len(keyword)].upper())
            key_index += 1
        else:
            key.append(letter)

    for i in range(len(ciphertext)):
        letter = ciphertext[i]
        if letter.islower():
            shift = ord(key[i]) - ord("A")
            plaintext += chr(((ord(letter) - shift - ord("a")) % 26 + ord("a")))
        elif letter.isupper():
            shift = ord(key[i]) - ord("A")
            plaintext += chr(((ord(letter) - shift - ord("A")) % 26 + ord("A")))
        else:
            plaintext += letter

    return plaintext
