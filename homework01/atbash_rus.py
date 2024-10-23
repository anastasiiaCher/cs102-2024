"""Реализация atbash"""

def encrypt_atbash(plaintext):
    alfabeto = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    alfabetoatbash = "".join(reversed(alfabeto))
    alfabetominuscole = alfabeto.lower()
    alfabetoatbash += "".join(reversed(alfabetominuscole))
    alfabeto = alfabeto + alfabetominuscole
    # print(alfabetoatbash)
    ciphered_text = ""
    # numero=0

    for char in plaintext:

        if char.isalpha():
            numero = alfabeto.index(char)
            ciphered_text += alfabetoatbash[numero]
        else:
            ciphered_text += char
    return ciphered_text


# print(encrypt_atbash("Привет Мир"))
