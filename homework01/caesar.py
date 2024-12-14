"""
Модуль для реализации шифра Цезаря.

Содержит функции для шифрования и расшифровки текста путем сдвига букв в алфавите на заданное количество позиций.
"""


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
        if char.isalpha():  # Проверяем, является ли символ буквой
            # Определяем базу для сдвига (для заглавных или строчных букв)
            base = ord("A") if char.isupper() else ord("a")
            # Сдвигаем символ
            new_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext += new_char
        else:
            # Не изменяем символ, если это не буква
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
        if char.isalpha():  # Проверяем, является ли символ буквой
            # Определяем базу для сдвига (для заглавных или строчных букв)
            base = ord("A") if char.isupper() else ord("a")
            # Обратный сдвиг
            new_char = chr((ord(char) - base - shift) % 26 + base)
            plaintext += new_char
        else:
            # Не изменяем символ, если это не буква
            plaintext += char
    return plaintext
