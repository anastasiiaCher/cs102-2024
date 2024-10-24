"""Caesar cipher system"""


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """Encrypting with C.c.s"""
    ciphertext = ""
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for plain in enumerate(plaintext):
        if plain[1] in alphabet:
            if ord(plain[1]) in range(97, 123):
                if ord(plain[1]) + shift > 122:
                    ciphertext += chr(ord(plain[1]) + shift - 26)
                else:
                    ciphertext += chr(ord(plain[1]) + shift)
            if ord(plain[1]) in range(65, 91):
                if ord(plain[1]) + shift > 90:
                    ciphertext += chr(ord(plain[1]) + shift - 26)
                else:
                    ciphertext += chr(ord(plain[1]) + shift)
        else:
            ciphertext += plain[1]
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """Decrypting with C.c.s"""
    plaintext = ""
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for cipher in enumerate(ciphertext):
        if cipher[1] in alphabet:
            if ord(cipher[1]) in range(97, 123):
                if ord(cipher[1]) - shift < 97:
                    plaintext += chr(ord(cipher[1]) - shift + 26)
                else:
                    plaintext += chr(ord(cipher[1]) - shift)
            if ord(cipher[1]) in range(65, 91):
                if ord(cipher[1]) - shift < 65:
                    plaintext += chr(ord(cipher[1]) - shift + 26)
                else:
                    plaintext += chr(ord(cipher[1]) - shift)
        else:
            plaintext += cipher[1]
    return plaintext
