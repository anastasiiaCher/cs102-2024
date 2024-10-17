"Данная функция шифрует и расшифровывает строку"


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
    keyword = (keyword * (len(plaintext) // len(keyword) + 1))[: len(plaintext)]
    for i, char in enumerate(plaintext):
        if char.isalpha() and char.isupper():
            shift = ord(keyword[i].upper()) - ord("A")
            ciphertext += chr(
                (ord(plaintext[i]) + shift)
                if ord(plaintext[i]) + shift in range(65, 91)
                else (ord(plaintext[i]) + shift) - 26
            )
        elif char.isalpha() and char.islower():
            shift = ord(keyword[i].lower()) - ord("a")
            ciphertext += chr(
                (ord(plaintext[i]) + shift)
                if ord(plaintext[i]) + shift in range(97, 123)
                else (ord(plaintext[i]) + shift) - 26
            )

        else:
            ciphertext += chr(ord(char))
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
    keyword = (keyword * (len(ciphertext) // len(keyword) + 1))[: len(ciphertext)]
    for i, char in enumerate(ciphertext):
        if char.isalpha() and char.isupper():
            shift = ord(keyword[i].upper()) - ord("A")
            plaintext += chr(
                (ord(ciphertext[i]) - shift)
                if ord(ciphertext[i]) - shift in range(65, 91)
                else (ord(ciphertext[i]) - shift) + 26
            )
        elif char.isalpha() and char.islower():
            shift = ord(keyword[i].lower()) - ord("a")
            plaintext += chr(
                (ord(ciphertext[i]) - shift)
                if ord(ciphertext[i]) - shift in range(97, 123)
                else (ord(ciphertext[i]) - shift) + 26
            )

        else:
            plaintext += chr(ord(char))
    return plaintext


print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))
