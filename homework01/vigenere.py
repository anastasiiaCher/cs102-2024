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

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    keyword_indices: list[int] = []
    text = list(plaintext)

    for char in keyword:
        if char.isalpha():
            keyword_indices.append(alphabet.index(char.lower()))

    for i, char in enumerate(text):
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shift = (alphabet.index(char.lower()) + keyword_indices[i % len(keyword_indices)]) % 26
            ciphertext += chr(base + shift)
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
    plaintext = ""

    alphabet = "abcdefghijklmnopqrstuvwxyz"
    keyword_indices: list[int] = []

    for char in keyword:
        if char.isalpha():
            keyword_indices.append(alphabet.index(char.lower()))

    for i, char in enumerate(ciphertext):
        if char.isalpha():
            base = ord("A") if char.isupper() else ord("a")
            shift = (alphabet.index(char.lower()) - keyword_indices[i % len(keyword_indices)] + 26) % 26
            plaintext += chr(base + shift)
        else:
            plaintext += char

    return plaintext
