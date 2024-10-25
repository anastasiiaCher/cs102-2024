def encrypt_affine(plaintext: str, a: int = 5, b: int = 1) -> str:
    m = ord("Я") - ord("А") + 1

    ciphertext = ""
    for ch in plaintext:
        symbol = ""

        if ord("А") <= ord(ch) <= ord("Я"):
            symbol = chr((a * (ord(ch) - ord("А")) + b) % m + ord("А"))
        elif ord("а") <= ord(ch) <= ord("я"):
            symbol = chr((a * (ord(ch) - ord("а")) + b) % m + ord("а"))
        else:
            symbol = ch
        ciphertext += symbol

    return ciphertext


def decrypt_affine(ciphertext: str, a: int = 5, b: int = 1) -> str:
    plaintext = ""
    for ch in ciphertext:
        symbol = ""

        if ord("А") <= ord(ch) <= ord("Я"):
            symbol = chr(((ord(ch) - ord("А") - b) // a) % (ord("Я") - ord("А") + 1) + ord("А"))
        elif ord("а") <= ord(ch) <= ord("я"):
            symbol = chr(((ord(ch) - ord("а") - b) // a) % (ord("я") - ord("а") + 1) + ord("а"))
        else:
            symbol = ch
        plaintext += symbol

    return plaintext


# text = "абВгД"
# print(encrypt_affine(text, 5, 1))
# print(decrypt_affine(encrypt_affine(text, 5, 1), 5, 1))
