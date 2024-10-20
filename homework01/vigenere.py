"""Модуль для работы с шифром Виженера"""


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
    keyword_full = (keyword * ((len(plaintext) // len(keyword)) + 1))[: len(plaintext)]
    for char, key_char in zip(plaintext, keyword_full):
        if char.isalpha():  # Проверяем, является ли символ буквой
            shift = ord(key_char.upper()) - ord("A")  # Определяем сдвиг для текущего символа ключа
            base = (
                ord("A") if char.isupper() else ord("a")
            )  # Определяем базовый код: 'A' для заглавных и 'a' для строчных букв
            new_char = chr((ord(char) - base + shift) % 26 + base)  # Шифруем символ и добавляем его в результат
            ciphertext += new_char
        else:
            ciphertext += char  # Если символ не буква, добавляем его в результат без изменений
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
    keyword_full = (keyword * ((len(ciphertext) // len(keyword)) + 1))[: len(ciphertext)]
    for char, key_char in zip(ciphertext, keyword_full):
        if char.isalpha():  # Проверяем, является ли символ буквой
            shift = ord(key_char.upper()) - ord("A")  # Определяем сдвиг для текущего символа ключа
            base = (
                ord("A") if char.isupper() else ord("a")
            )  # Определяем базовый код: 'A' для заглавных и 'a' для строчных букв
            new_char = chr((ord(char) - base - shift) % 26 + base)  # Расшифровываем символ и добавляем его в результат
            plaintext += new_char
        else:
            plaintext += char  # Если символ не буква, добавляем его в результат без изменений
    return plaintext
