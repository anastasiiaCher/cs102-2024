def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for char in plaintext:
        if 'A' <= char <= 'Z':
            # Сдвиг для заглавных букв
            shifted = (ord(char) - ord('A') + shift) % 26 + ord('A')
            ciphertext += chr(shifted)
        elif 'a' <= char <= 'z':
            # Сдвиг для строчных букв
            shifted = (ord(char) - ord('a') + shift) % 26 + ord('a')
            ciphertext += chr(shifted)
        else:
            # Остальные символы не меняются
            ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    for char in ciphertext:
        if 'A' <= char <= 'Z':
            # Обратный сдвиг для заглавных букв
            shifted = (ord(char) - ord('A') - shift) % 26 + ord('A')
            plaintext += chr(shifted)
        elif 'a' <= char <= 'z':
            # Обратный сдвиг для строчных букв
            shifted = (ord(char) - ord('a') - shift) % 26 + ord('a')
            plaintext += chr(shifted)
        else:
            # Остальные символы не меняются
            plaintext += char
    return plaintext