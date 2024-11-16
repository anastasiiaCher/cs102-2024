def encrypt_atbash(plaintext):
    alphabet = "0абвгдежзийклмнопрстуфхцчшщъыьэюя"
    ciphertext = ""

    for char in plaintext:
        if char.lower() in alphabet:
            i = alphabet.index(char.lower())
            if char.isupper():
                ciphertext += alphabet[-i].upper()
            else:
                ciphertext += alphabet[-i]
        else:
            ciphertext += char
    return ciphertext
