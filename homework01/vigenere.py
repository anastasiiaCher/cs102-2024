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
    key_index = 0  # Индекс для перебора символов ключа

    for char in plaintext:
        if char.isalpha():
            # Определяем сдвиг
            # Приводим символ ключа к верхнему регистру для удобства вычислений
            key_char = keyword[key_index % key_length].upper()
            shift = ord(key_char) - ord('A')

            if char.isupper():
                # Шифруем заглавную букву
                new_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                # Шифруем строчную букву
                new_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a'))

            ciphertext += new_char
            key_index += 1
        else:
            # Не меняем неалфавитные символы
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
    key_length = len(keyword)
    key_index = 0  # Индекс для перебора символов ключа

    for char in ciphertext:
        if char.isalpha():
            # Определяем сдвиг
            key_char = keyword[key_index % key_length].upper()
            shift = ord(key_char) - ord('A')

            if char.isupper():
                # Дешифруем заглавную букву
                new_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                # Дешифруем строчную букву
                new_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

            plaintext += new_char
            key_index += 1
        else:
            # Не меняем неалфавитные символы
            plaintext += char

    return plaintext