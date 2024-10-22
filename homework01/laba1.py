"""
Афинный шифр
"""


def encrypt_affine(plaintext: str, a: int, b: int) -> str:
    """
    Функция для шифровании строку с использованием аффинного шифра.
    """
    m = 26
    # Кол-во букв в английском алфавите
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            # Проверяем, является ли символ буквой
            char = char.lower()
            # Приводим символ к нижнему регистру
            x = ord(char) - ord("a")
            # Находим позицию символа в алфавите
            value = (a * x + b) % m
            # Заданная формула шифрования
            encrypted_text += chr(value + ord("a"))
            # Преобразуем обратно в символ
        else:
            # Если символ не является буквой, оставляем его без изменений
            encrypted_text += char

    return encrypted_text
