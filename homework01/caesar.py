"""модуль кодирования и декодирования по шифру цезаря"""


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
    for char in plaintext:
        if ord(char) in range(65, 91):
            ciphertext += chr((ord(char) - 65 + shift) % (26) + 65)
        elif ord(char) in range(97, 123):
            ciphertext += chr((ord(char) - 97 + shift) % (26) + 97)
        else:
            ciphertext += char
    return ciphertext


# print("введите что-то")
# print(encrypt_caesar(input()))


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
    i = 0
    for char in ciphertext:
        i += 1
        if ord(char) in range(65, 91):
            plaintext += chr((ord(char) - 65 - shift) % 26 + 65)
        elif ord(char) in range(97, 123):
            plaintext += chr((ord(char) - 97 - shift) % 26 + 97)
        else:
            plaintext += char
    return plaintext


# print(decrypt_caesar(input()))
