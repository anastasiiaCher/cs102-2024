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
    ciphertext = ""
    while len(keyword) < len(plaintext):
        for i in keyword:
            keyword += i
    keyword = keyword[: len(plaintext)]
    for i in range(len(plaintext)):
        shift1 = ord(keyword[i]) - ord("A")
        shift2 = ord(keyword[i]) - ord("a")

        if plaintext[i].isupper() and plaintext[i].isalpha():
            ciphertext += chr(ord("A") + ((ord(plaintext[i]) - ord("A") + shift1) % 26))
        elif plaintext[i].islower() and plaintext[i].isalpha():
            ciphertext += chr(ord("a") + ((ord(plaintext[i]) - ord("a") + shift2) % 26))
        else:
            ciphertext += plaintext[i]
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
    plaintext = ""
    while len(keyword) < len(ciphertext):
        for i in keyword:
            keyword += i
    keyword = keyword[: len(ciphertext)]
    for i in range(len(ciphertext)):
        shift1 = ord(keyword[i]) - ord("A")
        shift2 = ord(keyword[i]) - ord("a")
        if ciphertext[i].isupper() and ciphertext[i].isalpha():
            plaintext += chr(ord("A") + ((ord(ciphertext[i]) - ord("A") - shift1) % 26))
        elif ciphertext[i].islower() and ciphertext[i].isalpha():
            plaintext += chr(ord("a") + ((ord(ciphertext[i]) - ord("a") - shift2) % 26))
        else:
            plaintext += ciphertext[i]
    return plaintext


text2 = decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
print(text2)
