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
    keyword = keyword.upper()  # Преобразуем ключ в верхний регистр
    keyword_index = 0  # Индекс текущего символа в ключе

    for char in plaintext:
        if char.isalpha():  # Шифруем только буквы
            shift = ord(keyword[keyword_index % len(keyword)]) - ord("A")

            if char.isupper():  # Если буква заглавная
                new_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            else:  # Если буква строчная
                new_char = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))

            keyword_index += 1  # Переходим к следующему символу в ключе
        else:  # Символы, не являющиеся буквами, остаются неизменными
            new_char = char

        ciphertext += new_char  # Добавляем символ в результат

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
    keyword = keyword.upper()  # Преобразуем ключ в верхний регистр
    keyword_index = 0  # Индекс текущего символа в ключе

    for char in ciphertext:
        if char.isalpha():  # Дешифруем только буквы
            shift = ord(keyword[keyword_index % len(keyword)]) - ord("A")

            if char.isupper():  # Если буква заглавная
                new_char = chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
            else:  # Если буква строчная
                new_char = chr((ord(char) - ord("a") - shift) % 26 + ord("a"))

            keyword_index += 1  # Переходим к следующему символу в ключе
        else:  # Символы, не являющиеся буквами, остаются неизменными
            new_char = char

        plaintext += new_char  # Добавляем символ в результат

    return plaintext
