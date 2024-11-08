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

    keyword = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]

    for i, letter in enumerate(plaintext):
        if letter.isupper():
            ord_letter = ord(letter) + ord(keyword[i].upper()) - ord('A')
            if ord_letter > ord('Z'):
                ord_letter -= 26
            ciphertext += chr(ord_letter)
        elif letter.islower():
            ord_letter = ord(letter) + ord(keyword[i].lower()) - ord('a')
            if ord_letter > ord('z'):
                ord_letter -= 26
            ciphertext += chr(ord_letter)
        else:
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

    keyword = (keyword * (len(ciphertext) // len(keyword) + 1))[:len(ciphertext)]

    for i, letter in enumerate(ciphertext):
        if letter.isupper():
            ord_letter = ord(letter) - ord(keyword[i].upper()) + ord('A')
            if ord_letter < ord('A'):
                ord_letter += 26
            plaintext += chr(ord_letter)

        elif letter.islower():
            ord_letter = ord(letter) - ord(keyword[i].lower()) + ord('a')
            if ord_letter < ord('a'):
                ord_letter += 26
            plaintext += chr(ord_letter)
        else:
            plaintext += letter
    return plaintext
