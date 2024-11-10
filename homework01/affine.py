"""
Этот модуль реализует аффинный шифр для шифрования.
"""


def encrypt_affine(text, a_key, b_key):
    """
    Шифрует данный открытый текст с использованием аффинного шифра.

    Параметры:
    text (str): Текст для шифрования.
    a_key (int): Мультипликативный ключ.
    b_key (int): Аддитивный ключ.

    Возвращает:
    str: Зашифрованный текст.
    """
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    m = len(alphabet)

    def affine_encrypt_char(char, a_inner_key, b_inner_key):
        if char.lower() not in alphabet:
            return char
        x = alphabet.index(char.lower())
        encrypted_index = (a_inner_key * x + b_inner_key) % m
        encrypted_char = alphabet[encrypted_index]
        if char.isupper():
            return encrypted_char.upper()
        return encrypted_char

    ciphertext_result = "".join(affine_encrypt_char(char, a_key, b_key) for char in text)

    return ciphertext_result


# Пример использования
if __name__ == "__main__":
    plaintext = "Hello, world!"
    a = 5
    b = 8
    ciphertext = encrypt_affine(plaintext, a, b)
    print(ciphertext)
