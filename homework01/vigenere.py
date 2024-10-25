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
    count = 0  # вводим счетчик итераций, чтобы с каждой итерацией переходить к следующей букве кодового слова

    # Зашифровываем каждый элемент в исходном тексте:
    for char in plaintext:
        # вводим переменную для порядкового номера буквы в кодовом слове:
        current_letter_num = count % len(keyword)  # при этом проверяем, что нумерация не выходит за границы слова

        # Определяем сдвиг:
        if "A" <= keyword[current_letter_num] <= "Z":            # проверяем регистр кодовой буквы
            shift = ord(keyword[current_letter_num]) - ord("A")  # сдвиг равен коду буквы минус код буквы "А"
        elif "a" <= keyword[current_letter_num] <= "z":          # аналогично для строчных букв
            shift = ord(keyword[current_letter_num]) - ord("a")
        else:                                                    # обрабатываем случай, когда некий элемент
            print("Shift is not defined")                        # кодового слова не является буквой
            break

        # Получаем код зашифрованного элемента:
        if "A" <= char <= "Z":                                   # Если элемент шифруемой строки - прописная буква, то
            ord_new_char = ord(char) + shift                     # прибавляем сдвиг
            while ord_new_char > ord("Z"):                         # Если выходим за границы алфавита, то
                ord_new_char -= 26                               # сдвигаемся к началу
        elif "a" <= char <= "z":
            ord_new_char = ord(char) + shift                     # Аналогично для строчной буквы
            while ord_new_char > ord("z"):
                ord_new_char -= 26
        else:                                                    # Если элемент шифруемой строки - не буква, то
            ord_new_char = ord(char)                             # оставляем как есть

        ciphertext += chr(ord_new_char)  # записываем полученный элемент в строку с зашифрованным текстом
        count += 1                       # переходим к следующей букве в кодовом слове
    return ciphertext


encrypt_vigenere("ATTACKATDAWN", "LEMON")


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
    count = 0  # вводим счетчик итераций, чтобы с каждой итерацией переходить к следующей букве кодового слова

    # Дешифровываем каждый элемент зашифрованной строки:
    for char in ciphertext:
        # вводим переменную для порядкового номера буквы в кодовом слове:
        current_letter_num = count % len(keyword)  # при этом проверяем, что нумерация не выходит за границы слова

        # Определяем сдвиг:
        if "A" <= keyword[current_letter_num] <= "Z":            # проверяем регистр кодовой буквы
            shift = ord(keyword[current_letter_num]) - ord("A")  # сдвиг равен коду буквы минус код буквы "А"
        elif "a" <= keyword[current_letter_num] <= "z":          # аналогично для строчных букв
            shift = ord(keyword[current_letter_num]) - ord("a")
        else:                                                    # обрабатываем случай, когда некий элемент
            print("Shift is not defined")                        # кодового слова не является буквой
            break

        # Получаем код дешифрованного элемента:
        if "A" <= char <= "Z":                                   # Если элемент дешифруемой строки - прописная буква, то
            ord_new_char = ord(char) - shift                     # вычитаем сдвиг
            while ord_new_char < ord("A"):                       # Если выходим за границы алфавита, то
                ord_new_char += 26                               # сдвигаемся к концу
        elif "a" <= char <= "z":
            ord_new_char = ord(char) - shift                     # Аналогично для строчной буквы
            while ord_new_char < ord("a"):
                ord_new_char += 26
        else:                                                    # Если элемент дешифруемой строки - не буква, то
            ord_new_char = ord(char)                             # оставляем как есть

        plaintext += chr(ord_new_char)  # записываем полученный элемент в строку с дешифрованным текстом
        count += 1  # переходим к следующей букве в кодовом слове
    return plaintext
