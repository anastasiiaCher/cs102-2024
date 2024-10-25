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
        keyword += keyword
    if len(keyword) > len(plaintext):
        delta = len(keyword) - len(plaintext)
        keyword = keyword[:-delta]
    for i in range(len(plaintext)):
        if not plaintext[i].isalpha():
            ciphertext += plaintext[i]
            continue
        if plaintext[i].isspace():
            ciphertext += " "
            continue
        if plaintext[i] == plaintext[i].upper():
            strt = ord("A")
            ceil = ord("Z")
        else:
            strt = ord("a")
            ceil = ord("z")
        shift = (ord(keyword[i]) % strt) % 26
        ascii_index = ord(plaintext[i]) + shift
        if ascii_index > strt + 26:
            ascii_index = strt + (ascii_index - strt) % 26
        if ascii_index > ceil:
            ascii_index = strt - 1 + ascii_index - ceil
        ciphertext += chr(ascii_index)
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
    while len(keyword) < len(ciphertext):
        keyword += keyword
    if len(keyword) > len(ciphertext):
        delta = len(keyword) - len(ciphertext)
        keyword = keyword[:-delta]
    for i in range(len(ciphertext)):
        if not ciphertext[i].isalpha():
            plaintext += ciphertext[i]
            continue
        if ciphertext[i].isspace():
            plaintext += " "
            continue
        if ciphertext[i] == ciphertext[i].upper():
            strt = ord("A")
            ceil = ord("Z")
        else:
            strt = ord("a")
            ceil = ord("z")
        shift = (ord(keyword[i]) % strt) % 26
        ascii_index = ord(ciphertext[i]) - shift
        if ascii_index < strt:
            ascii_index = ceil + 1 - (strt - ascii_index)
        if ascii_index > ceil:
            ascii_index = strt - 1 + ascii_index - ceil
        plaintext += chr(ascii_index)
    return plaintext
