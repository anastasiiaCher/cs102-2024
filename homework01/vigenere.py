"""функци шифрования и дешифрования по Виженеру"""


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
    i = 0
    ciphertext = ""
    for char in plaintext:
        if i < len(keyword):
            shift = ord((keyword[i]).upper()) - 65
            i += 1
            if ord(char) in range(65, 91):
                ciphertext += chr((ord(char) - 65 + shift) % (26) + 65)
            elif ord(char) in range(97, 123):
                ciphertext += chr((ord(char) - 97 + shift) % (26) + 97)
            else:
                ciphertext += char
        else:
            i = 0
            shift = ord((keyword[i]).upper()) - 65
            if ord(char) in range(65, 91):
                ciphertext += chr((ord(char) - 65 + shift) % (26) + 65)
            elif ord(char) in range(97, 123):
                ciphertext += chr((ord(char) - 97 + shift) % (26) + 97)
            else:
                ciphertext += char
            i += 1
    return ciphertext


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
    i = 0
    for char in ciphertext:
        if i < len(keyword):
            shift = ord((keyword[i]).upper()) - 65
            i += 1
            if ord(char) in range(65, 91):
                plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
            elif ord(char) in range(97, 123):
                plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
            else:
                plaintext += char
        else:
            i = 0
            shift = ord((keyword[i]).upper()) - 65
            if ord(char) in range(65, 91):
                plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
            elif ord(char) in range(97, 123):
                plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
            else:
                plaintext += char
            i += 1
    return plaintext


print("введите текст и ключ для текста")
print(encrypt_vigenere(plaintext=input(), keyword=input()))
print(decrypt_vigenere(ciphertext=input(), keyword=input()))
