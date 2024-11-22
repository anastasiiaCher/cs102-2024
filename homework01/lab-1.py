def encrypt_atbash(plaintext):
    ciphertext = ""

    for char in plaintext:
        if "A" <= char <= "Z":
            # Заменяем заглавную букву на противоположную
            ciphertext += chr(ord("Z") - (ord(char) - ord("A")))
        elif "a" <= char <= "z":
            # Заменяем строчную букву на противоположную
            ciphertext += chr(ord("z") - (ord(char) - ord("a")))
        else:
            # Оставляем символы без изменений
            ciphertext += char

    return ciphertext


#  Пример использования
print(encrypt_atbash("Hello, World!"))
