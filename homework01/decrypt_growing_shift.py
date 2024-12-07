def decrypt_growing_shift(ciphertext: str, start: int, delta: int) -> str:
    """
    функция расшифровывающая особый шифр цезаря
    """
    plaintext = ""
    i = 0
    cons = start
    for char in ciphertext:
        i += 1

        if ord(char) in range(1040, 1072):

            plaintext += chr((ord(char) - 1040 - start) % (32) + 1040)
            start = start + delta
        elif ord(char) in range(1072, 1104):
            plaintext += chr((ord(char) - 1072 - start) % (32) + 1072)
            start = start + delta
        else:
            plaintext += char

    return plaintext


print("введите что-то")
a = input()
b = int(input())
c = int(input())

d = decrypt_growing_shift(a, b, c)
print(d)
