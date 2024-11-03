import math


def encrypt_scytale(plaintext, n):
    plaintext = plaintext.replace(" ", "")
    # ищем количество строк
    rows_num = math.ceil(len(plaintext) / n)
    # добиваемся того, чтобы у нас длина текста совпадала с количеством ячеек в нашей "таблице"
    padding_length = (rows_num * n) - len(plaintext)
    if padding_length > 0:
        plaintext += "*" * padding_length

    # создаем список, в котором будут хранится строки нашей таблицы
    rows = []
    # создаем цикл, в котором будут добавляться новые строки таблицы
    for i in range(0, len(plaintext), n):
        rows.append(plaintext[i : i + n])
    # создаем цикл, который будет печатать зашифрованный текст
    ciphertext = ""
    for i in range(n):
        for j in rows:
            ciphertext += j[i]

    return ciphertext
