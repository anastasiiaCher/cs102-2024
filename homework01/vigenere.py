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
    newkeyword = keyword * (len(plaintext) // len(keyword) + 1) if len(keyword) < len(plaintext) else keyword
    shift = [ord(x.lower()) - ord("a") for x in newkeyword]
    for i, letter in enumerate(plaintext):
        if letter.isupper() and letter.isalpha():
            if ord(letter) + shift[i] > ord("Z"):
                ciphertext += chr(ord(letter) + (shift[i] - 26))
            else:
                ciphertext += chr(ord(letter) + shift[i])
        elif letter.islower() and letter.isalpha():
            if ord(letter) + shift[i] > ord("z"):
                ciphertext += chr(ord(letter) + (shift[i] - 26))
            else:
                ciphertext += chr(ord(letter) + shift[i])
        elif not (letter.isalpha()):
            ciphertext += letter
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
    newkeyword = keyword * (len(ciphertext) // len(keyword) + 1) if len(keyword) < len(ciphertext) else keyword
    shift = [ord(x.lower()) - ord("a") for x in newkeyword]
    for i, letter in enumerate(ciphertext):
        if letter.isupper() and letter.isalpha():
            if ord(letter) - shift[i] < ord("A"):
                plaintext += chr(ord(letter) + (26 - shift[i]))
            else:
                plaintext += chr(ord(letter) - shift[i])
        elif letter.islower() and letter.isalpha():
            if ord(letter) - shift[i] < ord("a"):
                plaintext += chr(ord(letter) + (26 - shift[i]))
            else:
                plaintext += chr(ord(letter) - shift[i])
        elif not (letter.isalpha()):
            plaintext += letter
    return plaintext
