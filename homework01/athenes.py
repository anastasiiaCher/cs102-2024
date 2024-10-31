"""
Афинный шифр (рус)
"""


def encrypt_affine(plaintext: str, a: int, b: int) -> str:
    """
    Функция для шифровании строку с использованием аффинного шифра.
    """
    n = 33
    # Кол-во букв в русском алфавите
    encrypted_text = ""
    for i in plaintext:
        if i.isalpha():
            # Проверяем, является ли символ буквой
            if i.islower():
                # Проверяем регистр
                x = ord(i) - ord("а")
                # Находим позицию символа в алфавите
                shift = ord("а")
            else:
                x = ord(i) - ord("А")
                # Находим позицию символа в алфавите
                shift = ord("А")
            value = (a * x + b) % n
            # Заданная формула шифрования
            encrypted_text += chr(value + shift)
            # Преобразуем обратно в символ

        else:
            # Если символ не является буквой, оставляем его без изменений
            encrypted_text += i

    return encrypted_text
