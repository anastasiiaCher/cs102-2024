"""Модуль для работы с шифром Цезаря."""


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Определяем начало алфавита
            start = ord("A") if char.isupper() else ord("a")
            # Применяем сдвиг и рассчитываем новый код символа
            new_char = chr((ord(char) - start + shift) % 26 + start)
            ciphertext += new_char
        else:
            # Для символов, отличных от букв, просто добавляем как есть
            ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            # Определяем базовое значение в зависимости от регистра
            base = ord("A") if char.isupper() else ord("a")
            # Вычисляем позицию символа относительно алфавита и сдвигаем
            offset = ord(char) - base
            new_char = chr((offset - shift) % 26 + base)
            plaintext += new_char
        else:
            # Если не буква, добавляем символ без изменений
            plaintext += char
    return plaintext
