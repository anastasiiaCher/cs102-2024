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
    keyword_length = len(keyword)
    ciphertext = ""
    encryption_key = ""
    for i, char in enumerate(plaintext):
        if char.isalpha():
            encryption_key += keyword[i % keyword_length].lower()
        else:
            encryption_key += char

    for i, char in enumerate(plaintext):
        if char.isalpha():
            shift = ord(encryption_key[i].lower()) - ord("a")
            if char.islower():
                encrypted_char = chr((ord(char) - ord("a") + shift) % 26 + ord("a"))
            else:
                encrypted_char = chr((ord(char) - ord("A") + shift) % 26 + ord("A"))
            ciphertext += encrypted_char
        else:
            ciphertext += char

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
    keyword_length = len(keyword)
    plaintext = ""
    encryption_key = ""

    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            encryption_key += keyword[i % keyword_length].lower()
        else:
            encryption_key += ciphertext[i]

    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = ord(encryption_key[i].lower()) - ord("a")
            if char.islower():
                decrypted_char = chr((ord(char) - ord("a") - shift) % 26 + ord("a"))
            else:
                decrypted_char = chr((ord(char) - ord("A") - shift) % 26 + ord("A"))
            plaintext += decrypted_char
        else:
            plaintext += char

    return plaintext


print(encrypt_vigenere("ATTACKATDAWN", "LEMON"))
print(decrypt_vigenere("LXFOPVEFRNHR", "LEMON"))
