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
    k = 0
    newkeyword = keyword * (len(plaintext) // len(keyword) + 1) if len(keyword) < len(plaintext) else keyword
    shift = [ord(x.lower()) - ord("a") for x in newkeyword]
    for i in plaintext:
        if i.isupper() and i.isalpha():
            if ord(i) + shift[k] > ord("Z"):
                ciphertext += chr(ord(i) + (shift[k] - 26))
            else:
                ciphertext += chr(ord(i) + shift[k])
            k += 1
        elif i.islower() and i.isalpha():
            if ord(i) + shift[k] > ord("z"):
                ciphertext += chr(ord(i) + (shift[k] - 26))
            else:
                ciphertext += chr(ord(i) + shift[k])
            k += 1
        elif not (i.isalpha()):
            ciphertext += i
            k += 1
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
    k = 0
    newkeyword = keyword * (len(ciphertext) // len(keyword) + 1) if len(keyword) < len(ciphertext) else keyword
    shift = [ord(x.lower()) - ord("a") for x in newkeyword]
    for i in ciphertext:
        if i.isupper() and i.isalpha():
            if ord(i) - shift[k] < ord("A"):
                plaintext += chr(ord(i) + (26 - shift[k]))
            else:
                plaintext += chr(ord(i) - shift[k])
            k += 1
        elif i.islower() and i.isalpha():
            if ord(i) - shift[k] < ord("a"):
                plaintext += chr(ord(i) + (26 - shift[k]))
            else:
                plaintext += chr(ord(i) - shift[k])
            k += 1
        elif not (i.isalpha()):
            plaintext += i
            k += 1
    return plaintext
