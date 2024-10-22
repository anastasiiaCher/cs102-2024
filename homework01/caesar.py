"Данная функция шифрует и расшифровывает строку"


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
        if i.isalpha():
            decripted_i = ord(i) + shift
            if i.isupper():
                if decripted_i in range(65, 91):
                    ciphertext += chr(decripted_i)
                elif decripted_i in range(91, 97):
                    ciphertext += chr(decripted_i - 26)
                else:
                    ciphertext += chr(ord("A") + (decripted_i - 91))
            elif decripted_i in range(97, 123):
                ciphertext += chr(decripted_i)
            else:
                ciphertext += chr(ord("a") + (decripted_i - 123))
        else:
            ciphertext += i
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
    for i in ciphertext:
        if i.isalpha():
            decripted_i = ord(i) - shift
            if i.isupper():
                if decripted_i in range(65, 91):
                    plaintext += chr(decripted_i)
                elif decripted_i in range(0, 65):
                    plaintext += chr(decripted_i + 26)
                else:
                    plaintext += chr(90 - (decripted_i - 65))
            elif decripted_i in range(97, 123):
                plaintext += chr(decripted_i)
            elif decripted_i in range(0, 97):
                plaintext += chr(decripted_i + 26)
            else:
                plaintext += chr(122 - (decripted_i - 97))
        else:
            plaintext += i
    return plaintext


# print(decrypt_caesar('MnNfulvPqji`yUVN-ierspjhRsxJKXHH-uLKwuV,vLTpYGwlskuujGglnxJvQXWw', 13))
