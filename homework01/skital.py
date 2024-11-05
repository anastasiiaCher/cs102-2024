"""Данная функция выполняет шифр Скитала"""


def encrypt_scital(plaintext, n):
    """Это функция зашифровки"""
    m = (len(plaintext) + n - 1) // n

    table = [""] * m
    for i in range(len(plaintext)):
        row = i // n
        table[row] += plaintext[i]

    for i in range(m):
        while len(table[i]) < n:
            table[i] += "*"
    ciphertext = ""

    for col in range(n):
        for row in range(m):
            if col < len(table[row]):
                ciphertext += table[row][col]

    return ciphertext


def decrypt_scital(ciphertext, n):
    """Это функция расшифровки"""
    m = (len(ciphertext) + n - 1) // n

    table = [""] * n

    for i in range(len(ciphertext)):
        row = i // m
        table[row] += ciphertext[i]

    plaintext = ""

    for col in range(m):
        for row in range(n):
            if col < len(table[row]):
                plaintext += table[row][col]

    return "".join(plaintext.split("*"))


print(encrypt_scital("НАС АТАКУЮТ", 4), "|", decrypt_scital("НАУАТЮСАТ К*", 4))
