"""implementation of the encryption and decryption functions"""


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
    for i in plaintext:
        if i.isupper() and i.isalpha():
            ciphertext += chr(ord("A") + (ord(i) - ord("A") + 26 + shift) % 26)
        elif i.islower() and i.isalpha():
            ciphertext += chr(ord("a") + (ord(i) - ord("a") + 26 + shift) % 26)
        else:
            ciphertext += i

    return ciphertext


text1 = encrypt_caesar("Python3.6")
print(text1)


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
    for i in ciphertext:
        if i.isupper() and i.isalpha():
            plaintext += chr(ord("A") + (ord(i) - ord("A") + 26 - shift) % 26)
        elif i.islower() and i.isalpha():
            plaintext += chr(ord("a") + (ord(i) - ord("a") + 26 - shift) % 26)
        else:
            plaintext += i
    return plaintext


text2 = decrypt_caesar("sbwkrq")
print(text2)
