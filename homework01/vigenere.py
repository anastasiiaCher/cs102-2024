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
    key_index = 0

    for char in plaintext:
        key_char = keyword[key_index % key_length].lower()
        shift = ord(key_char) - ord('a')

        if char.isalpha():
            if char.isupper():
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            ciphertext += new_char
        else:
            # Неалфавитный символ - копируем без изменения
            ciphertext += char

        # Внимание: независимо от того, буква или нет, двигаем индекс ключа
        key_index += 1

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
    key_index = 0

    for char in ciphertext:
        key_char = keyword[key_index % key_length].lower()
        shift = ord(key_char) - ord('a')

        if char.isalpha():
            if char.isupper():
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            plaintext += new_char
        else:
            # Неалфавитный символ - копируем без изменения
            plaintext += char

        # Двигаем индекс ключа всегда
        key_index += 1

    return plaintext