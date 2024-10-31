"""implementation of the encryption and decryption functions"""


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

    keyword = keyword.upper()
    key_length = len(keyword)
    key_int = [ord(i) - ord("A") for i in keyword]
    plaintext_length = len(plaintext)

    ciphertext = ""

    for i in range(plaintext_length):
        char = plaintext[i]
        if char.isalpha():
            shift = key_int[i % key_length]
            if char.isupper():
                shifted = (ord(char) - ord("A") + shift) % 26
                ciphertext += chr(shifted + ord("A"))
            else:
                shifted = (ord(char) - ord("a") + shift) % 26
                ciphertext += chr(shifted + ord("a"))
        else:
            ciphertext += char
    return ciphertext


text1 = encrypt_vigenere("PYTHON", "A")


print(text1)


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
    keyword = keyword.upper()
    key_length = len(keyword)
    key_int = [ord(i) - ord("A") for i in keyword]
    ciphertext_length = len(ciphertext)

    plaintext = ""

    for i in range(ciphertext_length):
        char = ciphertext[i]
        if char.isalpha():
            shift = key_int[i % key_length]
            if char.isupper():
                shifted = (ord(char) - ord("A") - shift) % 26
                plaintext += chr(shifted + ord("A"))
            else:
                shifted = (ord(char) - ord("a") - shift) % 26
                plaintext += chr(shifted + ord("a"))
        else:
            plaintext += char

    return plaintext
