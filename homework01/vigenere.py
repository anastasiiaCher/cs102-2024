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

    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    keyword_ides = list(keyword)
    text = list(plaintext)

    for i in range(len(keyword_ides)):
        if keyword_ides[i].isalpha():
            keyword_ides[i] = alphabet.index(keyword_ides[i].lower())

    for i in range(len(text)):
        if text[i].isalpha():
            base = ord('A') if text[i].isupper() else ord('a')
            shift = (alphabet.index(text[i].lower()) + keyword_ides[i % len(keyword_ides)]) % 26
            ciphertext += chr(base + shift)
        else:
            ciphertext += text[i]

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
    # PUT YOUR CODE HERE
    return plaintext