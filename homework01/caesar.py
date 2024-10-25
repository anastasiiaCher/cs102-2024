def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for i in range(len(plaintext)):
        letter = plaintext[i]
        if letter.islower():
            chr(((ord(letter)+ shift - ord('a'))%26 + ord('a')))
        elif letter.isupper():
            ciphertext += chr(((ord(letter) + shift - ord("A"))%26 + ord("A")))
        else:
            ciphertext += letter
        
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
    for i in range(len(ciphertext)):
        letter = ciphertext[i]
        if letter.islower():
            plaintext += chr(((ord(letter) - shift - ord('a'))%26 + ord('a')))
        elif letter.isupper():
            plaintext += chr(((ord(letter) - shift - ord('A'))%26 + ord('A')))
        else:
            plaintext += letter
            return plaintext