"""
Модуль для реализации шифра Виженера.

Содержит функции для шифрования и расшифровки текста с использованием шифра Виженера.
"""


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
    # Повторяем ключ, если его длина меньше длины текста
    keyword_repeated = (keyword * (len(plaintext) // len(keyword) + 1))[: len(plaintext)]
    for p_char, k_char in zip(plaintext, keyword_repeated):
        if p_char.isalpha():  # Шифруем только алфавитные символы
            shift = ord(k_char.lower()) - ord("a")  # Рассчитываем сдвиг от 'a'
            if p_char.islower():
                ciphertext += chr((ord(p_char) - ord("a") + shift) % 26 + ord("a"))
            else:
                ciphertext += chr((ord(p_char) - ord("A") + shift) % 26 + ord("A"))
        else:
            ciphertext += p_char  # Неалфавитные символы остаются без изменений
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
    # Повторяем ключ, если его длина меньше длины текста
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword) + 1))[: len(ciphertext)]
    for c_char, k_char in zip(ciphertext, keyword_repeated):
        if c_char.isalpha():  # Расшифровываем только алфавитные символы
            shift = ord(k_char.lower()) - ord("a")  # Рассчитываем сдвиг от 'a'
            if c_char.islower():
                plaintext += chr((ord(c_char) - ord("a") - shift) % 26 + ord("a"))
            else:
                plaintext += chr((ord(c_char) - ord("A") - shift) % 26 + ord("A"))
        else:
            plaintext += c_char  # Неалфавитные символы остаются без изменений
    return plaintext
