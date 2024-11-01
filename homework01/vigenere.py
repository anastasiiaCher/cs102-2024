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
    keyword_repeated = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]

    for p, k in zip(plaintext, keyword_repeated):
        if p.isalpha():
            regist = ord('a') if p.islower() else ord('A')
            new = chr((ord(p) - regist + ord(k.lower()) - ord('a')) % 26 + regist)
            ciphertext += new
        else:
            ciphertext += p

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
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]

    for c, k in zip(ciphertext, keyword_repeated):
        if c.isalpha():
            regist = ord('a') if c.islower() else ord('A')
            new = chr((ord(c) - regist - (ord(k.lower()) - ord('a'))) % 26 + regist)
            plaintext += new
        else:
            plaintext += c

    return plaintext

encrypted = encrypt_vigenere(plaintext, keyword)
print(encrypted)

decrypted = decrypt_vigenere(encrypted, keyword)
print(decrypted)