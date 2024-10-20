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
    keyword_rep = (keyword * ((len(plaintext) // len(keyword)) + 1))[:len(plaintext)]

    for i in range(len(plaintext)):
        letter = plaintext[i]
        key_letter = keyword_rep[i]

        if 'A' <= letter <= 'Z':
            shift = ord(key_letter.upper()) - ord('A')
            ciphertext += chr((ord(letter) - ord('A') + shift) % 26 + ord('A'))
        elif 'a' <= letter <= 'z':
            shift = ord(key_letter.lower()) - ord('a')
            ciphertext += chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))
        else:
            ciphertext += letter
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
    keyword_rep = (keyword * ((len(ciphertext) // len(keyword)) + 1))[:len(ciphertext)]

    for i in range(len(ciphertext)):
        letter = ciphertext[i]
        key_letter = keyword_rep[i]

        if 'A' <= letter <= 'Z':
            shift = ord(key_letter.upper()) - ord('A')
            plaintext += chr((ord(letter) - ord('A') - shift) % 26 + ord('A'))
        elif 'a' <= letter <= 'z':
            shift = ord(key_letter.lower()) - ord('a')
            plaintext += chr((ord(letter) - ord('a') - shift) % 26 + ord('a'))
        else:
            plaintext += letter
    return plaintext
