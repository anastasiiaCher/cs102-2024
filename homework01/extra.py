def encrypt_affine(plaintext, a, b):
    ciphertext = ""
    for i in plaintext:
        if i.isalpha():
            if i.isupper():
                temp = chr(1040 + (((ord(i) - 16) % 32 * a + b) % 32))
            else:
                temp = chr(1072 + (((ord(i) - 16) % 32 * a + b) % 32))
            ciphertext += temp
        else:
            ciphertext += i
    return ciphertext
