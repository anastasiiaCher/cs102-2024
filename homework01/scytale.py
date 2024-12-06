"""Реализована функция шифра Скитала."""

import math


def encrypt_sctyale(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Scytale cipher.
    """
    ciphertext = ""
    plain_length = len(plaintext)
    cols = math.ceil(plain_length / shift)
    msg = [["" for j in range(shift)] for i in range(cols)]
    for i in range(plain_length):
        msg[i % cols][i // cols] = plaintext[i]
    ciphertext = "".join(["".join(map(str, _)) for _ in msg])
    ciphertext = ciphertext.replace(" ", "_")
    return ciphertext


def decrypt_scytale(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Scytale cipher.
    """
    cipher_length = len(ciphertext)
    cols = math.ceil(cipher_length / shift)
    msg = [["" for j in range(cols)] for i in range(shift)]
    for i in range(cipher_length):
        msg[i % shift][i // shift] = ciphertext[i]
    plaintext = "".join(["".join(map(str, _)) for _ in msg])
    plaintext = plaintext.replace("_", " ")
    return plaintext


print(encrypt_sctyale("РАКЕТНЫЕ ВОЙСКА", 3))
print(decrypt_scytale("РНОАЫЙКЕСЕ_КТВА", 3))
