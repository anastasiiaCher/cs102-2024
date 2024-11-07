def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    "SBWKRQ"
    >>> encrypt_caesar("python")
    "sbwkrq"
    >>> encrypt_caesar("Python3.6")
    "Sbwkrq3.6"
    >>> encrypt_caesar("")
    ""
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                if ord(char) < ord("z") - shift + 1:
                    ciphertext += chr(ord(char) + shift)
                else:
                    ciphertext += chr(ord(char) + shift - 26)
            else:
                if ord(char) < ord("Z") - shift + 1:
                    ciphertext += chr(ord(char) + shift)
                else:
                    ciphertext += chr(ord(char) + shift - 26)
        else:
            ciphertext += char
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    "PYTHON"
    >>> decrypt_caesar("sbwkrq")
    "python"
    >>> decrypt_caesar("Sbwkrq3.6")
    "Python3.6"
    >>> decrypt_caesar("")
    ""
    """
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                if ord(char) > ord("a") + shift - 1:
                    plaintext += chr(ord(char) - shift)
                else:
                    plaintext += chr(ord(char) - shift + 26)
            else:
                if ord(char) > ord("A") + shift - 1:
                    plaintext += chr(ord(char) - shift)
                else:
                    plaintext += chr(ord(char) - shift + 26)
        else:
            plaintext += char
    return plaintext
