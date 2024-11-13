def decrypt_scytale(ciphertext, shift):
    """Функция для расшивровки шифра скитала"""
    rows = len(ciphertext) // shift
    if len(ciphertext) % shift != 0:
        rows += 1
    table = [""] * rows
    for i in range(len(ciphertext)):
        """Вычисляется текущая строка, в которую нужно поместить
        символ и добавляется символ в текущую строку"""
        row = i % rows
        table[row] += ciphertext[i]
    plaintext = "".join(table)
    """ Объединяем строки, чтобы получить расшифрованный текст"""
    return plaintext
